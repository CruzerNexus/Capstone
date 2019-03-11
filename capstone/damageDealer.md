# **Damage-Dealer** A Star Wars: Armada Fleet Builder

## Project Overview
Damage-Dealer is an online list-builder app for people who play the Star Wars: Armada miniatures game.
### Major Features
Like many other fleet building apps, Damage Dealer offers a full catelogue of the game's various ship, squadron, upgrade, and objective cards as well as the functionality to use these cards to create a fully-printable fleet list.
Unlike other fleet builders, Damage-Dealer seeks to offer players a higher amount of information about the lists they create; most specifically, that fleet's expected damage output over the course of a game. I also plan to add other helpful calculations after succeeding in implementing the "Damage-Dealer Rating" such as fleet defensive stats, squadron-power, and commander-specific effectiveness.
### Libraries and Frameworks
I plan to go in-depth with skeleton or other CSS framework to make Damage-Dealer look professional and appealing to the eye (my main measure of success is to look at least as good as https://armada.ryankingston.com/ but add more color than just black and white). I also hope to make use of a competent database in order to store all the card information necessary to make the fleet builder functionality work.

## User Stories
### User 1: The Hobbyist
As an average Armada Player, I want a fleet builder which has a databases of all the cards in Star Wars Armada so I can create lists that are tournament legal and easy to modify and plan.
#### To-do
- Store ship/upgrade/squadron/objective cards in a model/db table
- Calculates list total.
- Nameable list.
- Print list (printable view)
    - Fleet Title
    - Point Total
    - Ships
        - Ship name
        - Upgrades
    - Squadrons
    - Objectives

### User 2: The Pro
As a professional Armada Player, I was a fleet builder that includes advanced details like my fleet’s overall damage output so that I know how much punch my fleet has.
#### To-do
- Calculate the combined damage output from all ships’ largest arcs at each range and find full average.
- Calculate the combined damage output from all squadrons with the “Bomber” keyword and/or squadrons with >50% chance of hitting and include that in the average.

### User 3: The Admiral on the Go
Having to always print my list is a bit of a hassle. I'd like to be able to save my lists to an online account so I can access them from any PC, tablet or phone.
#### To-do
- Create User accounts that will store a user's list(s) details online.
    - Allow Users to be able to save, view, and edit their lists on-site outside of initial creation.
    - Possibly allow the Users to publish their lists onsite to share with others who visit the site.

## Data Model
- User
- Cards
    - Ship
    - Squadron
    - Upgrade
    - Objective
- ImageSet
    - Card Images
    - Game-relevant symbols (make the site buttons look relevant and pretty)

## Schedule
- By the end of March 15th (Essential Features):
    - Have list-building functionality up and running
        - All cards in a database
        - Users can choose either "Rebel" or "Imperial" faction and begin building a list using cards in database.
        - Each ship can only equip upgrade cards that that type of ship can equip according to the rules.
        - Cards chosen add up to the total points added (where applicable) and display that near the top of the in-progress list.
        - Takes max damage outputs of all ship cards and adds them together to give the "Damage-Dealer Rating", displayed next-to or beneath the total points added.
        - "Print" functon translates chosen cards into a good-looking printable fleet list that fits a standard sheet of printer paper (or two, if necessary).
    - Site looks at least as good as Ryan Kingston's Armada Fleet Builder, if not better.
- By the end of March 22nd (Really-great-to-haves):
    - Have added User create, login, and List Library functionaliy
        - User can create an account
        - User can log into that account
        - User can store lists on-site in a personal database connected to their account
        - User can view, update, and save previously created lists
        - User can share their list on-site for other visitors to view.
    - Have added other calculation functionality
        - Fleet defensive stats
        - Squadron power
        - Fleet ship values
            - total command value
            - total squadron value
            - total engineering value
    - Have added filters for squadron keywords
- By the end of March 29th (Nice-to-haves):
    - Have added a Commander Rating
        - Depending on the commander being used, provide a rating based on the relevant stats of each ship in the list which make the commander's effect(s) more potent.
        - When clicked Include a brief  description that explains what stats are most relevant to that commander and why.
    - Have added an optional description box beneath the fleet name at the top where a user can describe their fleet and include it in the saved list.
    - Have an original logo to show off near the top of the site's home-page (A badge image depicting a vegas-style dealer offering the viewer a damage-card and smirking devilishly with a banner reading "Damage-Dealer" beneath).