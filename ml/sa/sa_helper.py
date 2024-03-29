import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def remove_user_handles(txt):
    return ' '.join(word for word in txt.split(' ') if not word.startswith('@'))


def save_as_json(dataframe, new_file_name):
    out = dataframe.to_json(orient='records', force_ascii=False)[1:-1]
    out = '[' + out + ']'

    with open(new_file_name + '.json', 'w', encoding='utf-8') as f:
        f.write(out)
    # dataframe.to_json(new_file_name + '.json', orient='records', lines=True)


def format_output(output_dict):
    polarity = "neutral"

    if output_dict['compound'] >= 0.05:
        polarity = "positive"

    elif output_dict['compound'] <= -0.05:
        polarity = "negative"

    return polarity


def main():
    # download vader model
    # nltk.download('vader_lexicon')

    df = pd.read_csv('../tweet_data/knust_twitter_dataset.csv')
    print(df.head())

    # cleaning the data of unneeded columns
    df = df.drop(columns=
                 ["hashtags/0", "hashtags/1", "hashtags/2", "hashtags/3", "hashtags/4", "media/0/media_url",
                  "media/0/type", "media/1/media_url", "media/1/type", "media/2/media_url", "media/2/type",
                  "media/3/media_url", "media/3/type", "startUrl", "url", "urls/0/display_url",
                  "urls/0/expanded_url", "urls/0/url", "user/advertiser_account_type", "user/blocked_by",
                  "user/blocking", "user/business_profile_state", "user/can_dm", "user/contributors_enabled",
                  "user/created_at", "user/default_profile_image", "user/description",
                  "user/ext_has_nft_avatar", "user/ext_is_blue_verified", "user/ext_verified_type",
                  "user/follow_request_sent", "user/followed_by", "user/following", "user/friends_count",
                  "user/geo_enabled", "user/has_custom_timelines", "user/id", "user/id_str",
                  "user/is_translation_enabled", "user/is_translator", "user/lang", "user/listed_count",
                  "user/location", "user/media_count", "user/muting", "user/normal_followers_count",
                  "user/notifications", "user/profile_background_color", "user/profile_background_image_url",
                  "user/profile_background_image_url_https", "user/profile_background_tile",
                  "user/profile_banner_extensions_sensitive_media_warning", "user/profile_banner_url",
                  "user/profile_image_extensions_sensitive_media_warning", "user/profile_image_url_https",
                  "user/profile_sidebar_border_color", "user/profile_sidebar_fill_color",
                  "user/profile_text_color", "user/profile_use_background_image", "user/protected",
                  "user/require_some_consent", "user/statuses_count", "user/time_zone", "user/translator_type",
                  "user/url", "user/utc_offset", "user/verified", "user/want_retweets",
                  "user_mentions/0/id_str", "user_mentions/0/name", "user_mentions/0/screen_name",
                  "user_mentions/1/id_str", "user_mentions/1/name", "user_mentions/1/screen_name",
                  "user_mentions/2/id_str", "user_mentions/2/name", "user_mentions/2/screen_name",
                  "user_mentions/3/id_str", "user_mentions/3/name", "user_mentions/3/screen_name",
                  "user_mentions/4/id_str", "user_mentions/4/name", "user_mentions/4/screen_name",
                  "user_mentions/5/id_str", "user_mentions/5/name", "user_mentions/5/screen_name",
                  "user_mentions/6/id_str", "user_mentions/6/name", "user_mentions/6/screen_name",
                  "user_mentions/7/id_str", "user_mentions/7/name", "user_mentions/7/screen_name",
                  "user_mentions/8/id_str", "user_mentions/8/name", "user_mentions/8/screen_name",
                  "user/fast_followers_count"])

    # remove user handles
    df['full_text'] = df['full_text'].apply(lambda x: remove_user_handles(x))

    # added dating
    df['date_sent'] = pd.to_datetime(df['created_at'])
    print(df['date_sent'])

    # extract date
    df['date'] = df['date_sent'].apply(lambda x: x.date())
    print(df['date'])

    # run vader analysis
    sentiment_analyzer = SentimentIntensityAnalyzer()

    df['sentiment_neg'] = df['full_text'].apply(lambda txt: sentiment_analyzer.polarity_scores(str(txt))['neg'])
    df['sentiment_pos'] = df['full_text'].apply(lambda txt: sentiment_analyzer.polarity_scores(str(txt))['pos'])
    df['sentiment_compound'] = df['full_text'].apply(
        lambda txt: sentiment_analyzer.polarity_scores(str(txt))['compound'])

    print(df.head())

    save_as_json(df, '../tweet_data/test1')


if __name__ == "__main__":
    main()
