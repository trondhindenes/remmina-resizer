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

if your resolution is 1920x1080 the last setting will be used, if not the default will be used.
This way you can tweak your settings even if you use the same computer with multiple screens, such as a large monitor at work and the built-in laptop screen at home.

If you don't create a settings file, remmina-resizer will default to the settings shown above (which means that the last setting is redundant and just meant as an example)

