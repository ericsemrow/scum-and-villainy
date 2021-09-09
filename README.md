# Scum and Villainy Bot

## Invite bot to your server
1. Click or copy the following link: [https://discord.com/api/oauth2/authorize?client_id=880614582782148669&permissions=11328&scope=bot](https://discord.com/api/oauth2/authorize?client_id=880614582782148669&permissions=11328&scope=bot)
2. Select your server from the dropdown and select "Continue"
3. Agree to the pre-selected permissions
4. Click "Authorize"

## Current commands

### Actions:
#### `![action] [number of dice]`

Scum and Villainy has 12 basic actions. Since the number of d6s you roll is often not the number in your stat block these rolls are not based on your current sheet. Rather you'll roll `![action] [num of dice]`

Actions include: attune, command, consort, doctor, hack, helm, rig, scramble, scrap, skulk, study, and sway

Ex. `!sway 2`

Rolling just `![action]` will assume 0 dice and therefore roll 2d6kl1

### Resistances
#### `![Resistance] [number of dice]`

The same format as action rolls. You'll roll a number of d6s which will deducted from 6. The resulting embedded message will tell you how much stress you add.

Resistances include: insight, prowess, resolve

Ex. `!prowess 1`

### Set
#### !set [position] [effect] [action] [user]

Before a player makes a roll you **set** the position and effect. This command will display an embed that will ping the user with the information you set. The arguments can be given in any order and none are required. Since the most common roll is Risky/Standard not providing position or effect will default to these values.

[position] - Only the first letter is required. Valid values are c (controlled), r (risky), d (desperate).
[effect] = Only the first letter is required. Valid values are l (limited), s (standard), g (great).
[action] = Any of the valid actions listed for the `!action` command.
[user] = A ping for a user with access to this channel. Ex. @coolguy123

Ex `!set sway r l @coolguy123`
Ex `!set @coolguy123 attune`

## Character Sheets

### Google Sheets
#### !gsheet [url]

**Make a copy** of this sheet: https://docs.google.com/spreadsheets/d/1SBI4wjgHUPNGEqmFlR3gY3SEzPh7e8sCA14ilQlXP-g
If you're u/B4ck_up14 shoot me a message!

Once you fill out the appropriate playbook make it the first sheet (position it furthest to the left). Grab the public link and run `!gsheet [url]`. It must be a valid public (read-only is fine) url in google drive. This will transfer your character to the bot.

### Sheet
#### !sheet

Prints a copy of your transferred sheet to that channel.

### XP
#### !xp [playbook or attribute] [value]

Adds or deducts xp from you character. PCs track XP for their playbook and any of the attributes listed in **Resistances**. Determine which one you're adding xp to and how much. Add it by running the command.

Ex. !xp playbook 2
Ex. !xp resolve 1
Oops, added too much
Ex. !xp prowess -1
