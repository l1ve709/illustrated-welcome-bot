## illustrated welcome bot 

this illustrated welcome bot creates a special png when a person enters and assigns it to the channel of your choice

## Language and Libraries Used

<picture>
  <source srcset="https://skillicons.dev/icons?i=py" media="(prefers-color-scheme: dark)">
  <img src="https://skillicons.dev/icons?i=py">
</picture>



### 1. `discord.py`
- **Purpose:** Interacts with Discord to handle events like member join, send messages, and execute commands.

### 2. `discord.ext.commands`
- **Purpose:** Adds command functionality to the bot (e.g., `.setchannel`).

### 3. `io`
- **Purpose:** Handles in-memory image files before sending them to Discord.

### 4. `Pillow (PIL)`
- **Purpose:** Edits images, resizes avatars, creates round profile pictures, and adds text to images.

### 5. `requests`
- **Purpose:** Fetches the avatar and background image from URLs.

## How to Run

1. Install the required libraries:
   ```bash
   pip install discord.py Pillow requests
   ```
2. Add your bot token:
   ```python
   l1ve709token = "YOUR TOKEN HERE"
   ```
3. Run the bot:
   ```bash
   python bot.py
   ```

## Commands

- **`.ayar [channel_id]`**: Sets the welcome message channel.

Make sure the bot has proper permissions in the target channel.
