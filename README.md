# Garden Planner

This project is a garden planner used to keep track of your seed inventory, planting dates, plant information and more. 
It also is a work in progress and doesn't really work yet. 




Some of the initial commits, before I migrated the project here for easier deployment, can be found [here](https://github.com/SwantjeM/garden-planner). 

## TODO deployment:

- create a new repo (on github -- [go here](https://github.com/new))
- git add/commit/push all of your code to this new repo
- go to [render.com](https://render.com/), go to "[Blueprints](https://dashboard.render.com/blueprints)" and click the "New Blueprint Instance" button. assuming that your github account is connected to your render account, connect your new repo with the new blueprint
  - set the `ALLOWED_HOSTS` value to the domain name you want to use and/or the `.onrender.com` sub-domain (see below). comma separate domains if you have multiple.
  - it can be confusing to do the previous step because you won't know which .onrender.com domain you'll be given when setting up the blueprint... uh... I guess you can write some domain in ALLOWED_HOSTS like example.com, do the render blueprint deployment, then see which domain you actually got, and then edit the ALLOWED_HOSTS value to the right .onrender.com domain... sorry, this is not perfect! TODO make it better.
- ok phew, you should be live!!!
- delete the contents of this readme and start anew; you could even add a little [powered by minimalish django starter](https://github.com/gregsadetsky/minimalish-django-starter) note at the bottom? but don't fret. TODO make the default readme not be the minimalish readme.

