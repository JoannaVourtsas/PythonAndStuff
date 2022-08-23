#classes and constructors/methodes and orject oriented variables

#class MyGame original source from https://api.arcade.academy/en/latest/examples/platform_tutorial/step_01.html 


import arcade

# Constants for Screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "My Cool Game"

#Constants for scale of sprites 
CHARACTER_SCALING = 0.1
TILE_SCALING = 0.5

MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self): #init runs everytime a object is created

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.AQUAMARINE)

    #gui camera is created to add a score board
    #this add a top layer to the window and wont be affected if character moves around
        self.gui_camera = None
        self.score = 0
#############################################
#Only Used for testing . Just Ignore        
        # Sprite lists
        #self.player_list = None
        #self.wall_list = None

        # Set up the player
        #self.player_sprite = None

        # This variable holds our simple "physics engine"
        #self.physics_engine = None

###########################################       

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

    # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.bear_list = arcade.SpriteList(use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        image_source = ":resources:images/animated_characters/Joanna Pics/stick.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        # Put some bears on the ground
        # This shows using a coordinate list to place sprites
        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
            # Add a obsticals on the ground (aka bears)
            bear = arcade.Sprite(
                ":resources:images/animated_characters/Joanna Pics/teddy.png", TILE_SCALING
            )
            bear.position = coordinate
            self.bear_list.append(bear)



        #Set up Gui camera to keep score
        self.gui_camera = arcade.Camera(self.width, self.height)

            
    def on_draw(self):
        """Render the screen."""

        self.clear()

        
        # Code to draw the screen goes here
        self.wall_list.draw()
        self.player_list.draw()
        self.bear_list.draw()



        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()

        # Draw score on the screen
        score_text = f"Score: {self.score}"
        #The f in front of strings tells Python to look at the values inside {}
        #and substitute them with the values of the variables if exist
        arcade.draw_text(score_text,10,10,arcade.csscolor.WHITE,18)

    #Control Character
    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if key == arcade.key.UP:
            self.player_sprite.change_y = 5
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -5
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
    #Stops character from cont going up/down , left/right
    def on_key_release(self, key, modifiers):
       
        if key == arcade.key.UP or key == arcade.key.DOWN:
         self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
            

    #update is need to keep checking for changes and to apply them
    def update(self, delta_time):
        """ Movement and game logic """

        self.player_list.update()
        self.player_list.update_animation()


        # Generate a list of all sprites that collided with the player.
        hit_list =  arcade.check_for_collision_with_list(self.player_sprite,self.bear_list)

        # Loop through each colliding sprite, remove it
        for bear in hit_list:
            bear.kill()
            self.score = self.score + 1

            

def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
