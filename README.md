# Pico Micropython Examples

This is the playground for my implementation and adaptation of the exercises in the book
`Get Started With Micropython on Raspberry Pi Pico`.

You will need to copy `kfkonrad.py` to your Pico in order for the scripts to work.

## Interacting with the filesystem

To use the custom libraries you will need to copy them over to you Pico first.
I recommend `ampy` for interactions with the Pico's filesystem. To install `ampy` run `pip install ampy`.

Run these commands to set up an alias for easier access. Your `PICO_DEVICE_PATH` will probably be different.

```sh
export PICO_DEVICE_PATH=/dev/tty.usbmodem223101
alias ampy="ampy -p $PICO_DEVICE_PATH"
```

### View files on the Pico

```sh
ampy  ls
```

### Copy a file or folder (recursively) to the Pico

```sh
ampy put kfkonrad.py
```

### Remove a file or empty directory

```sh
ampy rm kfkonrad.py
```

### Remove a directory recursively

```sh
ampy rmdir myfolder
```

### Print contents of a single file

```sh
ampy get kfkonrad.py
```

### Copy file from Pico to computer

```sh
ampy get kfkonrad.py kfkonrad.py
```

## Executing code from command line

The commands in this section *do* work, but I recommend using an IDE such as VS Code with the Pico-W-Go Plugin
or Thonny for added convenience.

### Run a script

This command does not allow for input but it will show output.

```sh
ampy run filename.py
```

Use `ampy run -n` to run the script in the background.
Press <kbd>Control</kbd> + <kbd>C</kbd> to stop showing the output and `ampy reset` to soft reset (reboot) and
stop the script if necessary.

### Connect to serial console

```sh
screen $PICO_DEVICE_PATH
```

Press <kbd>Control</kbd> + <kbd>A</kbd> then <kbd>K</kbd> then <kbd>Y</kbd> to exit screen.
