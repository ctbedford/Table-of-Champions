import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      try {
        const refreshToken = localStorage.getItem('refresh_token');
        const response = await axios.post(`${API_URL}/token/refresh/`, { refresh: refreshToken });
        localStorage.setItem('access_token', response.data.access);
        api.defaults.headers['Authorization'] = `Bearer ${response.data.access}`;
        return api(originalRequest);
      } catch (refreshError) {
        console.error('Error refreshing token:', refreshError);
        // Logout user if refresh token is invalid
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        window.location.href = '/login';
      }
    }
    return Promise.reject(error);
  }
);

export const login = async (username, password) => {
  try {
    const response = await api.post('/token/', { username, password });
    localStorage.setItem('access_token', response.data.access);
    localStorage.setItem('refresh_token', response.data.refresh);
    return response.data;
  } catch (error) {
    console.error('Login error:', error.response ? error.response.data : error.message);
    throw error;
  }
};


export const logout = () => {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
};

export const getLastUpdate = async () => {
  try {
    const response = await api.get('/last-update/');
    return response.data.length > 0 ? response.data[0] : null;
  } catch (error) {
    console.error('Error fetching last update:', error);
    return null;
  }
};

export const postTweet = async () => {
  const response = await api.post('/post-tweet/');
  return response.data;
};

export const getTemplates = async () => {
  const response = await api.get('/templates/');
  return response.data;
};

export const updateTemplate = async (show, content) => {
  const response = await api.put(`/templates/${show}/`, { show, content });
  return response.data;
};

export const syncTemplate = async (show) => {
  const response = await api.post('/sync-template/', { show });
  return response.data;
};

export const getPokerData = async () => {
  try {
    const response = await api.get('/poker-data/');
    return response.data;
  } catch (error) {
    console.error('Error fetching poker data:', error);
    throw error;
  }
};

