# Remmina-Resizer

A helper utility to update Remmina RDP connections with the right screen resolution

### How it works
Remmina is a great RDP client, but it lacks the option to dynamically adjust the screen size   
of connections depending on the "physical" monitor size.
remmina-resizer fixes this by looking at your current screen resolution, and   
adjusts the resolution of all remmina RDP connections dynamically.
Simply put, run remmina-resizer before you connect, and you should be good.

### Settings
You can optionally add a settings file in your home dir (path should be `$HOME/.remmina-resizer.yml`). Mine looks like this:   


```yaml
default:
  reduce_width: 40
  reduce_height: 111
1920x1080:
  reduce_width: 40
  reduce_height: 111
```

if your resolution is 1920x1080 the last setting will be used, if not the default will be used. You can add as many items to your settings file as you'd like, indicating each by the pixel resolution of your screen (such as `1920x1080`)
This way you can tweak your settings even if you use the same computer with multiple screens, such as a large monitor at work and the built-in laptop screen at home.

### What it does:
Given the above config: if you're on a computer where the screen's resolution is 1920x1080, remmina-resizer will subtract 40 by 111 pixels from the   
rdp session's screen size. This seems to be working well on Ubuntu 17, but it's up to you to tweak it to your liking and will depend on the size of your taskbar etc.

Remmina-resizer will only adjust RDP-type connections.

If you don't create a settings file, remmina-resizer will default to the settings shown above (which means that the last setting is redundant and just meant as an example).

### How to install
Install using pip/pip3: `(sudo) pip install remmina-resizer`


### How to run
run `remmina-resizer`. Note that any active RDP sessions will not be resized on the fly, you have to disconnect/reconnect to the session before the changes are activated. It's probably smart to just run remmina-resizer each time you've switched to another display, or have added RDP connections to Remmina.
Also note that editing a connection inside Remmina seems to reset the edited connection to its original value, so also run remmina-resizer after you've edited a connection.