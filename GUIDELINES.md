# Guidelines

These are the guidelines for contributions to Tread.

### Keep Master Clean

No one likes constantly rebasing their branches when code changes in the master branch. Direct commits to the master branch should only be non–code related.

### Intentful Branches

Topic branches should only address their topic. This is because, the more changes you make, the higher the chance that there will be merge conflicts. The purpose of branches is to isolate specific changes. If you find a bug or something while you're working in a topic branch, switch to another.

### Intentful Commits

In most views of the revision history, only the summary of each is visible. For this reason, your commit summaries should not be synopses. If you can't fit the all the changes you've made into a the summary line, it's a sign you need to split the commit into multiple.

### Push as often as possible, but no more

Pushing changes is great since people can view your progress. However, if the history of your branch doesn't look as good as you'd like, once you push it there's no way to fix it. For example, if you need to rebase your topic branch because of large changes in master, your only option would be to delete the remote branch.

### PRs should be created by the person in charge of the topic branch

Even though GitHub shows that annoying message when a branch had recent commits, resist the urge to create a Pull Request. Since only the person responsible for the topic branch can write an effective message, or know whom to request a review from, they should be the one to make the PR.

### PRs should be merged by the person in charge of the compare branch, unless a review was requested

Though a merge can be undone, it's messy and tarnishes the reflog. Instead, the person responsible for the compare branch (who should have authored the PR as well; see above) should be the one to merge it, to prevent unfinished/untested work from entering the master branch.

This guideline does not apply when a review was requested. Since reviews should only be requested when the author feels that the PR is ready to be merged, if all of the reviewers have approved, the PR should be merged as soon as possible.

### Delete the branch when you merge a PR

Having extraneous branches that have already been merged adds clutter to the Branch Chooser on GitHub. For this reason, branches should be deleted after they're merged.

Additionally, you should notify your teammates when you delete a branch so they can delete it locally. It's confusing, especially for new Git users, to have branches that aren't synced with remote.

### NEVER FORCE-PUSH

Force-pushing is never the answer. Everyone else in your team will inevitably hate you for it. Instead, use `git push --force-with-lease`. This will fail if your force-push would override others' work. If it does fail, you need to consider if what you're trying to do is really necessary.