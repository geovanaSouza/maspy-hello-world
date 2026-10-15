# maspy-hello-world

Small playground for experimenting with MASPY agent creation and belief updates.

## Experiments

1. Create the agent with the triggering belief already present.
2. Create the agent without a belief, then add it with `add()` before `start_system()`.
3. Add the belief after `start_system()` using a background thread and `instant=True`.