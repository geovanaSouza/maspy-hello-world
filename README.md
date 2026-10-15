# maspy-hello-world

Small playground for experimenting with MASPY agent creation and belief updates.

## Run

```bash
make setup
make run
```

`make help` lists all available commands.

## Experiments

- [x] 1. Create the agent with the triggering belief already present in its creation.
- [x] 2. Create the agent without a belief, then add it with `add()` before `start_system()`.
- [x] 3. Add the belief after `start_system()` using a background thread.
- [x] 4. Test an atomic plan.
- [x] 5. Make the `bye` plan depend on `hello`.