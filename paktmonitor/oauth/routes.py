from paktmonitor.oauth import oauth
from paktmonitor import paktmonitor
from flask_discord import DiscordOAuth2Session, requires_authorization, Unauthorized

discord = DiscordOAuth2Session(paktmonitor)

@oauth.route("/login")
def login():
    return discord.create_session()
	

@oauth.route("/callback")
def callback():
    discord.callback()
    return redirect(url_for(".me"))


@oauth.errorhandler(Unauthorized)
def redirect_unauthorized(e):
    return redirect(url_for("login"))

	