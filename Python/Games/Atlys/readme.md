# Atlys Game

Single Player Open World 2D Pirate Survival Game.

## TODO
- **Create Interface**
- **Start Consdering Save Options (Local SQLite Database?)**
- **How to Handle Persistence?**
  - Possibly Lists of items that load in around the player's immediate vicinity, no use loading things the character cannot see.
  - The loading should take place as the character is moving. We will do the following:
  - All items in the 9 screens connected to the player will load. As the player moves it will check if the items are in the range and will load and unload them as necessary.
  - Monsters will not move if the player is not within range to save execution of logic.
- **Start Considering Mapping Options**
  - Map should be large enough to feel like an open world and allow the player to explore and build. The ocean should be endless and come back on itself for circumnavigation.
  - Possibly use Perlin Noise to generate the landmasses and draw the maps.
- **Character Creation**
  - Would love to have multiple options, male and female.
- **Combat System**

