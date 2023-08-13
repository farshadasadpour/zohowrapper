def generate_url(botname, token):
    """

    Args:
        botname: the bot name
        token: for send to zoho

    Returns: completed url

    """
    requrl = f"https://cliq.zoho.com/company/767068114/api/v2/bots/{botname}/incoming?zapikey={token}"
    return requrl
