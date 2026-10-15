# maspy-hello-world

Small playground for experimenting with MASPY agent creation and belief updates.

## Run

```bash
make setup
make run
```

`make help` lists all available commands.

## Experiments

1. Create the agent with the triggering belief already present in its creation.
2. Create the agent without a belief, then add it with `add()` before `start_system()`.
3. Add the belief after `start_system()` using a background thread.
4. Test an atomic plan.
5. Make the `bye` plan depend on `hello`.