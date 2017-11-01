from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SelectField
from wtforms.validators import DataRequired, Email


class OptionsForm(FlaskForm):
    enabled = BooleanField('Enable Bridge?', default=True)

    post_to_twitter = BooleanField('Post to Twitter?', default=True)
    split_twitter_messages = BooleanField('Split messages on Twitter?', default=True)

    post_to_mastodon = BooleanField('Post to Mastodon?', default=True)
    toot_visibility = SelectField('Toot visibility',
                                  choices=[
                                      ('public', 'Public'),
                                      ('private', "Private"),
                                      ('unlisted', 'Unlisted'),
                                  ],
                                  default='public')


class MastodonIDForm(FlaskForm):
    mastodon_id = StringField('Enter your Mastodon ID', validators=[DataRequired(), Email()])
