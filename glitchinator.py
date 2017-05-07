#!/usr/bin/env python3

# glitchinator
# requires imageio, click, jpglitch

# Example usage:
# python3 glitchinator.py --frame_count 15 --output jerry_glitch --input jerry.png

import os, random, time
import jpglitch
import click
import imageio

def glitch_to_gif(src, frame_count=15, out=None):
	if out == None:
		out = 'glitchinator_'+str(time.time())
	if not os.path.exists('tmp'):
		os.mkdir('tmp')
	out += '.gif'
	frames = []
	
	img_data = imageio.imread(src)
	img_data = imageio.imwrite(imageio.RETURN_BYTES, img_data, format='JPEG-PIL')
	for glitch_count in range(frame_count):
		seed = random.randint(0, 99)
		amount = random.randint(0, 3)
		iterations = random.randint(0, 25)
		image_bytes = bytearray(img_data)
		fail = False
		jpeg = None
		filename = 'glitch_'+str(glitch_count).zfill(3)+'.jpg'
		try:
			jpeg = jpglitch.Jpeg(image_bytes, amount, seed, iterations)
		except Exception as e:
			print(e)
			fail = True
		if jpeg is not None:
			try:
				jpeg.save_image(os.path.join('tmp',filename))
				frames.append(filename)
			except Exception as e:
				print(e)
				fail = True
		else:
			fail = True
		if fail and os.path.exists(filename):
			os.remove(filename)
	if len(frames) > 0:
		with imageio.get_writer(out, mode='I') as writer:
			for filename in frames:
				image = imageio.imread(os.path.join('tmp', filename))
				writer.append_data(image)
				os.remove(os.path.join('tmp', filename))
	print('Saved '+out)
@click.command()
@click.option('--frame_count', '-f', type=click.IntRange(0, 99, clamp=True),
              default=15, help="Amount of glitched frames.")
@click.option('--output', '-o', help="Output filename for your glitched gif, with no extension.")
@click.argument('input_image', type=click.File('rb'))
def cli(input_image, frame_count, output):
	glitch_to_gif(input_image, frame_count, output)

if __name__ == '__main__':
	cli()