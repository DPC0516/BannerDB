import discord

banned_sentences = []
banned_words = []

command_ban_sentence = "!ban_s"
command_ban_word = "!ban_w"
command_print_ban_sentence = "!print_ban_s"
command_print_ban_word = "!print_ban_w"
command_help = "!help"

help_string = "This is bot for word, sentence ban system in discord" + \
              "\nProgrammed By DPC0516" + \
              "\nDevelopment Date: 2021 1 3" + \
              "\nCommands: " + \
              "\n!ban_s:[sentence] - bans sentences in []" + \
              "\n!ban_w:[word] - bans words in []" + \
              "\n!print_ban_s - prints banned sentences" + \
              "\n!print_ban_w - prints banned words" + \
              "\n!help - prints help menu"


class ChatBot(discord.Client):

    async def on_ready(self):
        game = discord.Game("금지 메시지 감시")

        await client.change_presence(status=discord.Status.online, activity=game)
        print("READY")

    async def on_message(self, message):
        if message.author.bot:
            return None

        message_str = message.content
        channel = message.channel

        if message_str.find("!") != -1:
            if message.author.guild_permissions.administrator:
                if message_str.find(command_ban_sentence) != -1:
                    try:
                        sentence = message_str.split(':')[1]
                    except Exception:
                        await channel.send("adding ban sentence has been failed")
                        return None

                    banned_sentences.append(sentence)
                    await channel.send("ban sentence '" + sentence + "' has been added successfully")
                    return None

                elif message_str.find(command_ban_word) != -1:
                    try:
                        word = message_str.split(':')[1]
                    except Exception:
                        await channel.send("adding ban word has been failed")
                        return None

                    banned_words.append(word)
                    await channel.send("ban word '" + word + "' has been added successfully")
                    return None
                else:
                    await channel.send("command " + message_str + " has not found")

            if message_str.find(command_help) != -1:
                await channel.send(help_string)
                return None

            elif message_str.find(command_print_ban_sentence) != -1:
                banned_sentences_string = "banned sentences:\n"
                for i in range(0, len(banned_sentences)):
                    banned_sentences_string += banned_sentences[i] + "\n"
                await channel.send(banned_sentences_string)
                return None

            elif message_str.find(command_print_ban_word) != -1:
                banned_words_string = "banned words:\n"
                for i in range(0, len(banned_words)):
                    banned_words_string += banned_words[i] + "\n"
                await channel.send(banned_words_string)
                return None

            else:
                await channel.send("command " + message_str + " has not found")

        for i in range(0, len(banned_sentences)):
            if banned_sentences[i] == message_str:
                await message.delete()
                return None

        for i in range(0, len(banned_words)):
            if message_str.find(banned_words[i]) != -1:
                await message.delete()
                return None

    async def on_message_edit(self, before, after):
        if after.author.bot:
            return None

        message_str = after.content
        channel = after.channel

        if message_str.find("!") != -1:
            if after.author.guild_permissions.administrator:
                if message_str.find(command_ban_sentence) != -1:
                    try:
                        sentence = message_str.split(':')[1]
                    except Exception:
                        await channel.send("adding ban sentence has been failed")
                        return None

                    banned_sentences.append(sentence)
                    await channel.send("ban sentence '" + sentence + "' has been added successfully")
                    return None

                elif message_str.find(command_ban_word) != -1:
                    try:
                        word = message_str.split(':')[1]
                    except Exception:
                        await channel.send("adding ban word has been failed")
                        return None

                    banned_words.append(word)
                    await channel.send("ban word '" + word + "' has been added successfully")
                    return None
                else:
                    await channel.send("command " + message_str + " has not found")

            if message_str.find(command_help) != -1:
                await channel.send(help_string)
                return None

            elif message_str.find(command_print_ban_sentence) != -1:
                banned_sentences_string = "banned sentences:\n"
                for i in range(0, len(banned_sentences)):
                    banned_sentences_string += banned_sentences[i] + "\n"
                await channel.send(banned_sentences_string)
                return None

            elif message_str.find(command_print_ban_word) != -1:
                banned_words_string = "banned words:\n"
                for i in range(0, len(banned_words)):
                    banned_words_string += banned_words[i] + "\n"
                await channel.send(banned_words_string)
                return None

            else:
                await channel.send("command " + message_str + " has not found")

        for i in range(0, len(banned_sentences)):
            if banned_sentences[i] == message_str:
                await after.delete()
                return None

        for i in range(0, len(banned_words)):
            if message_str.find(banned_words[i]) != -1:
                await after.delete()
                return None


client = ChatBot()
client.run("")
