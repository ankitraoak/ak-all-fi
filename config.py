#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Ak

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    AUTH_USERS = os.environ.get("AUTH_USERS")
    Log_channel = int(os.environ.get("Log_channel"))
