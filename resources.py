import pyglet


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

pyglet.resource.path = ["./resources"]  # resources localization
pyglet.resource.reindex()

player_image = pyglet.resource.image("player.png")
ball_image = pyglet.resource.image("ball.png")

center_image(player_image)
center_image(ball_image)
