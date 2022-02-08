#Discord bot command.
#Sends a message to the members of a project.

from bot_modules.config import jsonUsersRegisteredPath

from bot_modules.utils import readJSONFileAsDict

#OBS This function consider that the first project is the one that the manager is responsible.
async def endSprint(context):
    #Gets the ID of the person who called the command.
    requestUserID = str(context.author.id)

    #Get all users registered.
    users = readJSONFileAsDict(jsonUsersRegisteredPath)

    #Get the info of the user that called.
    requestUserInfo = None
    for user in users:
        if user == requestUserID:
            userInfo = users[user]
            break

    #Check permissions.
    if userInfo is not None:
        targetProject = None

        if "Gerente de Projeto" in userInfo["roles"]:
            targetProject = userInfo["projects"][0]
        
            if targetProject is not None:

                #TODO This is not efficient. But should work for a small team.
                #Checks all users registered to send a DM.
                for user in users:
                    if targetProject in users[user]["projects"]:
                        targetUser = await context.message.guild.fetch_member(int(user))

                        if targetUser is not None:
                            await targetUser.send("AEEEEEEEEEEEEEE")
                        else:
                            #TODO Log this in a file.
                            print("[endSprint] Usuário não encontrado no servidor para enviar DM.")

            else:
                await context.send("Você precisa fazer parte de um projeto como gerente.")

        else:
            await context.send("Você não tem permissão para invocar esse comando (para gerentes).")


    else:
        await context.send("Se cadastre antes de utilizar esse comando!")
    

