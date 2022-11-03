# AAP Usage 101

## Create project

Ensure that the *Git Sync* is successful (*Details > Last Job Status > Successful*).

## Run the template

> If you are the `admin` user, log out and log in as your previously created user!

**Launch the template...**


The playbook ran "successful", but nothing really happened, the play got skipped (*Could not match supplied host pattern*). Fix the error!

<p>
<details>
<summary><b>Help wanted?</b></summary>
 
Remember that every play always targets a group of hosts. Do we even defined a group in our inventory?

</details>
</p>

<p>
<details>
<summary><b>More help wanted?</b></summary>
 
The playbook targets the group `mkdocs`, create this group in your inventory (*Community Call Inventory*) and add `mkdocs-host` to that group. You will need to login as the *admin* user again, because you only have *read* permissions on the inventory.  
Log in as your personal user again and run the job template again.

</details>
</p>

Errors fixed? Look at the last task and input the IP address into your browser.

**Let the discussion begin!**