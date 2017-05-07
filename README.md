# glitchinator

Creates an animated glitch GIF from a source image

![example input](https://raw.githubusercontent.com/Spyduck/glitchinator/master/jerry.png)

![example output](https://raw.githubusercontent.com/Spyduck/glitchinator/master/glitchinator_1494194256.2830412.gif)

## Installation:

requires python 3, imageio, click, jpglitch:

> pip install imageio click git+https://github.com/NotSoSuper/jpglitch

## Example usage:
> python3 ./glitchinator.py --frame_count 15 --output ./jerry_glitch --input ./jerry.png
