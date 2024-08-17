import json


def generate_tweet():
    # Load the scraped data
    with open('highroll_poker_data.json', 'r') as f:
        players = json.load(f)

    # Sort players by net winnings (removing $ and , for proper numeric sorting)
    players.sort(key=lambda x: float(x['net_winnings'].replace(
        '$', '').replace(',', '')), reverse=True)

    # Create the Twitter post
    twitter_post = "Top HighRoll Poker Players:\n\n"
    for player in players[:5]:  # Limit to top 5 players
        twitter_post += f"{player['name']
                           }: {player['net_winnings']} ({player['bb_per_hour']})\n"

    twitter_post += "\nFull stats: https://highrollpoker.com/tracker/players"

    # Ensure the post is within Twitter's character limit
    if len(twitter_post) > 280:
        twitter_post = twitter_post[:277] + "..."

    print(twitter_post)
    print(f"\nCharacter count: {len(twitter_post)}")

    # Save the post to a file
    with open('twitter_post.txt', 'w') as f:
        f.write(twitter_post)

    return twitter_post


if __name__ == "__main__":
    generate_tweet()
