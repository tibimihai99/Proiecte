
#-----Import modules and initialize engine
import pygame,os,sys,random,json,copy
pygame.mixer.pre_init(44100, -16, 1, 1024)
pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "1" #Center the gaming window
pygame.display.set_caption("Pytris")
SCREEN_WIDTH,SCREEN_HEIGHT = 500,500
GAME_WINDOW = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
GAME_CLOCK = pygame.time.Clock()
GAME_TIME = 0
DELTATIME = 0
FRAME_RATE = 60
FROZEN = False
RUNTIME = True

#-----Load and handle game files
assets = {}
assets_path = os.path.join(".","assets","")
for f in os.listdir(assets_path):
	#Get every file in resource directory as a string with split extension
	k = f.split(".")
	
	#Check what kind of file it is and load it accordingly
	val = assets_path+f
	
	if "jpg" in k[1] or "jpeg" in k[1]: val = pygame.image.load(val).convert()
	elif "png" in k[1]: val = pygame.image.load(val).convert_alpha()
	elif "wav" in k[1]: val = pygame.mixer.Sound(val)
	else:pass
	
	assets.update({k[0]:val})
def FileData(file_name="blank_file",mode="r",data={},create_file=True,delete_file=False):
	"""Read/write JSON file data\n
	create_file: make a blank file with the name if the file isn't there\n
	delete_file: self explanitory"""
	path = assets_path+file_name+".json"
	valid = os.path.isfile(path)
	
	if valid:
		if delete_file:
			os.remove(path)
			return True
	
	if not valid:
		#No file named at this path
		if delete_file:return False
		if not create_file:
			#Don't create the blank file, just return a fail
			return False
		print(f"'{str.capitalize(file_name)}' file not found. Creating new one in: {assets_path}")
		mode = "w"
	with open(path,mode,encoding="utf-8") as f:
		if mode == "w":
			json.dump(data,f,indent=4)
			print(f"'{str.capitalize(file_name)}' file saved to: {path}")
			print(json.dumps(data,indent=4))
			return data
		elif mode == "r":
			data = dict(json.load(f))
			print(f"'{str.capitalize(file_name)}' file loaded successfully")
			print(json.dumps(data,indent=4))
			return data
		else:
			print("Error: mode should be either read or write.")

#-----Classes which hold settings, gameplay, resources, parts, and functionality
class Audio:
	"""Controls game audio, including volume, sound and music playing - with loop control"""

	sound_volume = 1
	music_volume = 1
	music_loops = -1
	__music_fresh = False
	
	#Control volume of either sound or music, or both
	@classmethod
	def Volume(cls,vol=0,change_sound=True,change_music=True):
		if change_sound:
			cls.sound_volume = vol
		if change_music:
			cls.music_volume = vol
			pygame.mixer_music.set_volume(vol)
	
	#One-shot play a sound
	@classmethod
	def PlaySound(cls,sound):
		sound.set_volume(cls.sound_volume)
		sound.play()

	#Load a music track to play
	@classmethod
	def LoadMusic(cls,music_file):
		pygame.mixer_music.load(music_file)
		cls.__music_fresh = True
	
	#Play or pause the music track
	@classmethod
	def PlayMusic(cls,play=True):
		if play:
			if cls.__music_fresh:
				pygame.mixer_music.play(cls.music_loops)
				cls.__music_fresh = False
			else:pygame.mixer_music.unpause()
		else:pygame.mixer_music.pause()

	#Freeze all audio in a paused state
	@classmethod
	def Freeze(cls,pause=True):
		if pause:
			pygame.mixer.pause()
			cls.PlayMusic(False)
		else:
			pygame.mixer.unpause()
			cls.PlayMusic()
class Graphics:
	"""Variables for colors, window structure, and fonts"""

	render_fps = False
	resolutions = [500,600,800]
	window_icon = pygame.display.set_icon(assets["icon"])
	window_half_coord1 = (0,0)
	window_half_coord2 = (SCREEN_WIDTH//2,0)
	window_mirror = False
	window_flicker_effect = False
	grid_style = 0
	
	#Colors
	color_black = (0,0,0)
	color_white = (255,255,255)
	color_grey = (128,128,128)
	#Set1
	color_red = (255,0,0)
	color_orange = (255,128,0)
	color_yellow = (255,255,0)
	color_green = (0,255,0)
	color_cyan = (0,255,255)
	color_blue = (0,0,255)
	color_purple = (128,0,128)
	#Set2
	color_salmon = (198,113,113)
	color_chocolate = (139,69,19)
	color_olive = (128,128,0)
	color_spring = (0,255,127)
	color_sea = (143,188,143)
	color_teal = (56,142,142)
	color_magenta = (255,0,255)
	#Fonts
	font_yuge = pygame.font.Font(assets["font_tetris"],60)
	font_mega = pygame.font.Font(assets["font_tetris"],35)
	font_large = pygame.font.Font(assets["font_roboto"],30)
	font_mid = pygame.font.Font(assets["font_roboto"],25)
	font_small = pygame.font.Font(assets["font_roboto"],18)
	#Transparent surface
	trans_surf = (255,255,255,200)
class Shapes:
	"""Shape data of the individual game pieces (index0 is color, 1-4 is structure)"""
	
	Z = [
		Graphics.color_red,
		["00.",
		 ".00",
		 "..."
		],
		["..0",
		 ".00",
		 ".0."
		],
		["...",
		 "00.",
		 ".00"
		],
		[".0.",
		 "00.",
		 "0.."
		]
	]
	L = [
		Graphics.color_orange,
		["..0",
		 "000",
		 "..."
		],
		[".0.",
		 ".0.",
		 ".00"
		],
		["...",
		 "000",
		 "0.."
		],
		["00.",
		 ".0.",
		 ".0."
		]
	]
	O = [
		Graphics.color_yellow,
		["00",
		 "00"
		],
		["00",
		 "00"
		],
		["00",
		 "00"
		],
		["00",
		 "00"
		]
	]
	S = [
		Graphics.color_green,
		[".00",
		 "00.",
		 "..."
		],
		[".0.",
		 ".00",
		 "..0"
		],
		["...",
		 ".00",
		 "00."
		],
		["0..",
		 "00.",
		 ".0."
		]
	]
	I = [
		Graphics.color_cyan,
		["....",
		 "0000",
		 "....",
		 "....",
		],
		["..0.",
		 "..0.",
		 "..0.",
		 "..0."
		],
		["....",
		 "....",
		 "0000",
		 "...."
		],
		[".0..",
		 ".0..",
		 ".0..",
		 ".0.."
		]
	]
	J = [
		Graphics.color_blue,
		["0..",
		 "000",
		 "..."
		],
		[".00",
		 ".0.",
		 ".0."
		],
		["...",
		 "000",
		 "..0"
		],
		[".0.",
		 ".0.",
		 "00."
		]
	]
	T = [
		Graphics.color_purple,
		[".0.",
		 "000",
		 "..."
		],
		[".0.",
		 ".00",
		 ".0."
		],
		["...",
		 "000",
		 ".0."
		],
		[".0.",
		 "00.",
		 ".0."
		]
	]
	
	shapes = [Z,L,O,S,I,J,T]
class Tetromino:
	"""Base object for a game piece"""

	#Called on instantiate, or whenever the piece moves or rotates
	def __GenerateShape(self,shape_x,shape_y,shape_data,rotate_data):
		
		#Generate grid x/y coordinates from the shape data
		shape_coords = []
		shape_form = shape_data[rotate_data]
		
		#Enumerate shape data row by row
		for r,value in enumerate(shape_form):
			#Current row ready to be dissected further
			row = list(value)
			
			for c, column in enumerate(row):
				#Check each item inside the row for a '0'
				if column == "0":
					#Add x/y coordinates taking into account the cell size of the board and current position of the tetromino
					shape_coords.append((shape_x+c,shape_y+r))
		
		#Data has been trimmed and each '0' has become an x/y coordinate ready to be drawn later as a rect
		return shape_coords
	
	def __init__(self,x=0,y=0,shape=Shapes.shapes[0]):
		#x/y coordinates is drawn as: one unit = one cell instead of one pixel
		self.x = x
		self.y = y
		self.shape = shape
		self.color = shape[0]
		self.rotation = 1
		self.block_positions = self.__GenerateShape(self.x,self.y,self.shape,self.rotation)
	
	#Handle independent moving and rotating the piece cell-by-cell
	def Move(self,x_direction=0,y_direction=0):
		self.x += x_direction
		self.y += y_direction
		
		#Need to regenerate the shape with the correct position
		self.block_positions = self.__GenerateShape(self.x,self.y,self.shape,self.rotation)
	
	def Rotate(self,clockwise=True):
		#Cycle through the shape list (1-4) to get rotated version of piece
		if clockwise:
			self.rotation += 1
			if self.rotation > 4:self.rotation = 1
		
		else:
			self.rotation += -1
			if self.rotation < 1:self.rotation = 4
		
		#Need to regenerate the shape with the correct rotation
		self.block_positions = self.__GenerateShape(self.x,self.y,self.shape,self.rotation)
class Board:
	"""Game board area variables"""
	coords = [0,0] #Pixel coords of the game board (top-left)
	grid = []
	height = SCREEN_HEIGHT
	width = SCREEN_WIDTH//2
	size_x = 10 #Number of cells
	size_y = 20 #In each dimension
	color_gridlines = (64,64,64) #Grid lines
	color_outline = Graphics.color_grey #Edge of board
	color_empty = Graphics.color_black #Empty cells - cant be exact same color as any tetromino
	outline_width = 2
	overlay_draw = False
	overlay_color = Graphics.color_white
class Hud:
	"""Gameplay heads up display window area"""
	coord = [0,0]
	height = SCREEN_HEIGHT
	width = SCREEN_WIDTH//2
	title = pygame.transform.smoothscale(assets["title_logo"],(210,60))

	#Next piece window
	next_tetromino = None
	nextpiece_window_size = (120,80)
	nextpiece_window_color = Graphics.color_grey
	nextpiece_window_width = 2
	nextpiece_block_size = 20
	nextpiece_text = Graphics.font_large.render("Next",True,Graphics.color_grey)

	#Score visuals
	score_text_points = Graphics.font_mid.render("Score: ",True,Graphics.color_white)
	score_text_lines = Graphics.font_mid.render("Lines: ",True,Graphics.color_white)
	score_text_level = Graphics.font_mid.render("Level: ",True,Graphics.color_white)
	controls_title = Graphics.font_large.render("Controls",True,Graphics.color_grey)

	#Text for controls
	controls_text = (
		(
			Graphics.font_small.render("Arrows/Z   =   Move/Rotate",True,Graphics.color_white),
			Graphics.font_small.render("Spacebar   =   Drop Piece",True,Graphics.color_white),
			Graphics.font_small.render("Enter/Return   =   Pause",True,Graphics.color_white),
			Graphics.font_small.render("Esc/R   =   Quit/Restart",True,Graphics.color_white),
			Graphics.font_small.render("S   =   Settings Menu",True,Graphics.color_white),
		),
		(
			Graphics.font_small.render("Y   =   Yes",True,Graphics.color_white),
			Graphics.font_small.render("N   =   No",True,Graphics.color_white),
		)
	)
class Gameplay:
	"""Holds gameplay state, gameplay values, and tetromino piece variables"""
	game_paused = False
	game_difficulty = 1 #Changes difficulty on reset of the game
	saved_difficulty = 1 #Difficulty that player may have changed mid-game - will become new difficulty on new game

	#Level change handling
	level_threshold = 10 #Number of cleared lines needed to increase level
	level_speedup_init = 1 #Number of cells the piece will fall per second at the start
	level_speedup_factor = 0.4 #Piece fall speed increaser with each level up
	level_flicker_active = False #When player increases level, have the level text in the HUD flicker
	level_flicker_speed = 0.5
	level_flicker_intervals = 6
	level_flicker_toggle = False

	#Panic - for when the player has filled up the board too much and it's looking grim
	panic_active = False
	panic_grid_threshold = 4 #Equals the top fractional of the grid rows (2 is top half, 4 is top quarter, 5 is top fifth, etc)

	#Gameover handling
	gameover_active = False
	gameover_screen_active = False
	gameover_threshold = 0 #The player piece grid y positions must be below this number to trigger a game over
	gameover_final_score = []
	gameover_highscores = {}
	gameover_board_drop = False #Board will do it's drop sequence while true
	gameover_board_accel = 8 #How fast the board drops exponentially
	gameover_board_speed = 1 #Current speed the board is moving in pixels - should start as 1
	gameover_text_color = Graphics.color_black
	gameover_text_flicker = False
	gameover_text_title = Graphics.font_mega.render("GAME OVER",True,gameover_text_color)
	gameover_text_highscore = Graphics.font_mid.render("HIGHSCORES",True,gameover_text_color)
	gameover_text_replay = Graphics.font_small.render("Play Again? (Y/N)",True,gameover_text_color)
	
	#Countdown timer handling
	countdown_active = False
	countdown_timer = 3 #The number that the countdown timer start counting down from
	countdown_speed = 0.5 #Number of seconds it takes to count down from one number to the next
	countdown_current_time = countdown_timer #Current state of the timer
	countdown_text_color = Graphics.color_white
	
	#Player piece, ghost, and user control handling
	player_tetromino = None
	prior_tetromino_coords = []
	piece_spawn_x, piece_spawn_y = -2,-2 #Cell coords where the top-left of the piece spawns (from top-center of grid)
	piece_horizontal_speed = 30 #Cells per second
	piece_vertical_speed = 30 #Ditto
	piece_horizontal_delay = 0.1 #Amount of delay between moving piece once and repeating fire while input key held down
	piece_vertical_delay = 0.2 #Ditto (currently not used)
	piece_horizontal_repeat_active = False #On when delay finishes
	piece_vertical_repeat_active = False #Ditto
	piece_fall_active = True #Should the piece be falling down?
	piece_fall_speed = 1 #Current cells per second for falling
	piece_lock_speed = 1 #How fast the piece gets locked into position (0 is never)
	line_clear_speed = 0.02 #How fast the lines clear in seconds (0 is near instant)
	line_clear_flicker_speed = 0.02 #How fast the side window flickers when player gets a Tetris clear
	random_tetromino_bag = []
	bag_piece_count = 1 #Number of pieces each in a random bag
	ghost_tetromino_active = True
	ghost_tetromino = None
	
	#Pause screen handling
	pause_screen_active = False
	pause_text = (
		Graphics.font_yuge.render("Python",True,Graphics.color_black),
		Graphics.font_yuge.render("Tetris",True,Graphics.color_black),
		Graphics.font_small.render("Code by Slevoacă Tiberiu",True,Graphics.color_black),
		Graphics.font_small.render("Tetris by Alexey Pajitnov",True,Graphics.color_black),
		
		Graphics.font_small.render("Press 'Spacebar' to play",True,Graphics.color_red)
	)
class Score:
	"""Current score, level, etc of the game"""

	current_score = 0
	current_level = 1
	cleared_lines = 0
	down_points = 1 #Increase score per cell when moving piece down
	drop_points = 2 #Same but sudden
	line_scores = [100,300,500,1000] #Score increases when clearing line amount (multiplied by level number)
	
	#Read and write to/from the highscores file in the assets folder
	score_file_name = "highscores"
	max_save_scores = 5
	
	#Collect score data from scores file
	@classmethod
	def GetScores(cls):
		data = FileData(cls.score_file_name,"r",create_file=False)
		
		if not data:
			#No highscore file - create one with bottom scoring
			blank_data = {}
			
			for num in range(cls.max_save_scores):
				blank_data.update({num+1:[0,0,0]})
			
			return FileData(cls.score_file_name,"w",blank_data)
		
		return data
	
	#Save the current score stats to the scores file if it made the cut
	@classmethod
	def SaveScore(cls):
		score_data = [x[1] for x in list(cls.GetScores().items())]
		score_stats = [Gameplay.game_difficulty,cls.cleared_lines,cls.current_score] #Scoring collected from finished game
		
		#Insert score into highscores if it made the cut
		for stat in range(len(score_data)):
			
			#First, check game difficulty - higher difficulty is better than bigger score
			if score_stats[0] >= score_data[stat][0]:
				if score_stats[0] > score_data[stat][0]:
					score_data.insert(stat,score_stats)
					break
				
				#Check score points
				if score_stats[2] >= score_data[stat][2]:
					if score_stats[2] > score_data[stat][2]:
						score_data.insert(stat,score_stats)
						break
					
					#Finally, check the lines cleared - fewer lines meant more efficient play
					if score_stats[2] == score_data[stat][2] and score_stats[1] < score_data[stat][1]:
						score_data.insert(stat,score_stats)
						break
					
					score_data.insert(stat+1,score_stats)
					break
		
		new_data = {}
		
		for num in range(cls.max_save_scores):
			new_data.update({num+1:score_data[num]})
		
		#Write final scoring
		FileData(cls.score_file_name,"w",new_data)

		#Return result of the score being in the highscores list
		if score_stats in score_data:return score_stats
		else:return False
	
	#Delete score file for fresh default stats
	@classmethod
	def DeleteScoreFile(cls):
		return FileData(cls.score_file_name,delete_file=True)
class GameTimer:
	"""Uses pygame event queue to post a timer event that will be set off at the appropriate time. Create a timer with SetTimer and check if it went off by either having it inside the game loop with an if statement or by listening to pygame events. Needs the 'Update' function to be called every game loop.\n
	USAGE:\n
	GameTimer.SetTimer(name_of_timer,etc...)\n
	Elsewhere...\n
	if event.type == USEREVENT: <- listening for the event\n
		if event.GameTimerEvent == <name of timer>: <-\n
			Success!\n
	Also:\n
	Some update loop:\n
		if GameTimer.SetTimer(name_of_timer,etc...): <- bool\n
			Success!"""

	__timer_list = []
	__time = 0.0
	__dt = 0.0
	
	class __TimerObj:
		def __init__(self,timer_id,duration,intervals):
			self.id = timer_id
			self.duration = duration
			self.intervals = intervals

			self.triggered = False
			self.paused = False
			self.pause_duration = 0
			self.countdown = duration
			self.lifetime = intervals
	
	@classmethod
	def __CalculateFrameDifference(cls,timer_duration):
		"""Allows for framerate independent timing so that the (relatively) correct amount of event/function firings occur regardless of low framerate or not."""
		try:
			i = int(cls.__dt / timer_duration) + 1
		except ZeroDivisionError:
			i = 0
		if i > 10:i = 10 #Sanity check - prevents unnecessary overloading of the pygame event queue
		return i

	@classmethod
	def Update(cls,current_time,deltatime):
		"""Call inside of a pygame loop that uses timers. The loop will need to have events, game ticks in seconds, and millisecond deltatime. There is no need to call it more than once per loop. Updates all timers so they count down and fire properly.\n
		E.g.\n
		deltatime = clock.tick() / 1000\n
		time = pygame.time.get_ticks() / 1000 ---OR--- time += deltatime\n
		GameTimer.Update(time, deltatime)"""

		cls.__time = current_time
		cls.__dt = deltatime

		for timer in cls.__timer_list:
			
			#See if timer is at end of it's life
			if timer.lifetime == 0:
				#Timer is exhausted
				timer.triggered = False
				continue
			
			#Handle the timer if paused
			if timer.pause_duration <= 0 and timer.paused:
				if timer.pause_duration <= -1:
					continue
				timer.paused = False
				continue
			elif cls.__time >= timer.pause_duration:timer.paused = False

			#Decrease timer if not paused
			if not timer.paused:
				timer.countdown -= cls.__dt

			#Fire timer
			if timer.countdown <= 0:

				#Check if framerate has a factor in number of event firings
				framerate_factor = cls.__CalculateFrameDifference(timer.duration)
				for x in range(framerate_factor):
					#Post the timer event(s)
					ev = pygame.event.Event(pygame.USEREVENT,GameTimerEvent=timer.id)
					pygame.event.post(ev)

				#Render timer as being fired and briefly return to main loop so that timer can trigger as true
				timer.triggered = True
				
				#Another loop - rewind the timer
				timer.countdown = timer.duration
				timer.lifetime -= 1
			else:
				timer.triggered = False

	@classmethod
	def GetTimer(cls,timer_id):
		"""Get timer object information from a named timer."""
		for timer in cls.__timer_list:
			if timer.id == timer_id:
				return timer

	@classmethod
	def SetTimer(cls,timer_id,duration=1.0,intervals=1):
		"""Make a new timer that creates an event and returns true every time it counts down and then stops after duration and intervals are exhausted. Only one instance of a named timer can exist at a time in the list. It is fine to call this function every frame from anywhere in the script and have the timer still work. Timer will stop after it's last interval, but will still be on the list. To restart the timer, call RemoveTimer on it and the next time the timer gets called, it will start again with the properties called on SetTimer. To reset a timer with different duration/intervals, simply modify those arguments on this function and the old timer will be removed and replaced. Returns true when the timer goes off and is safe to use as a conditional. NOTE: A timer with constantly changing arguments won't ever count down!\n
		timer_id = str name of timer object\n
		duration: per second - how long it takes the timer to fire / <=0 is pointless\n
		intervals: >0 = number of times the timer goes off before finally stopping / 0 = none / -1 = indefinite"""

		if not isinstance(timer_id,str):
			raise TypeError("Argument 'timer_id' must be a string")

		#Check if there's already a timer by that name in the list
		for timer in cls.__timer_list:
			if timer_id in timer.id:
				#Look through properties to see if anything changed
				if duration != timer.duration or intervals != timer.intervals:
					cls.RemoveTimer(timer.id)
					break

				#This timer has gone off
				if timer.triggered:
					return True

				#Nothing changed - same timer still ticking down
				return False
		
		#Make a new timer
		new_timer = cls.__TimerObj(timer_id,duration,intervals)
		cls.__timer_list.append(new_timer)

		return False

	@classmethod
	def PauseTimer(cls,timer_id,duration=0):
		"""Pause a named timer for a length of time. Call this function again to change pause duration for the timer to something else. To unpause, set duration to 0 and wait a frame. This function does nothing if the timer in question doesn't exist.\n
		timer_id = str\n
		duration: >0.0 = timed pause in seconds / 0 = pause for one loop (also effectively unpause) / -1 = pause indefinitely"""

		for timer in cls.__timer_list:
			if timer.id == timer_id:
				timer.paused = True
				if duration > 0:timer.pause_duration = cls.__time + duration

	@classmethod
	def RemoveTimer(cls,timer_id):
		"""Manually stop a timer and remove it from the list. Returns true if it removed the timer. The timer will be restarted if SetTimer is called again for it from somewhere.\n
		timer_id = str"""

		if not isinstance(timer_id,str):
			raise TypeError("Argument 'timer_id' must be a string")
		
		for timer in cls.__timer_list:
			if timer.id == timer_id:
				cls.__timer_list.remove(timer)
				return True
		
		return False
class Settings:
	"""Holds game settings to be set independently or from the settings menu screen"""

	settings_loaded = False
	settings_file_name = "settings"
	menu_active = False
	menu_background_color = Graphics.color_black
	menu_title = Graphics.font_mega.render("Settings",True,Graphics.color_cyan)
	menu_title_controls = Graphics.font_large.render("Controls",True,Graphics.color_grey)
	menu_color_setting = Graphics.color_green
	menu_color_items = Graphics.color_white
	menu_color_highlight = Graphics.color_yellow
	menu_controls = (
		Graphics.font_small.render("Up/Down  =  Select Setting",True,Graphics.color_white),
		Graphics.font_small.render("Left/Right  =  Change Setting",True,Graphics.color_white),
		Graphics.font_small.render("S  =  Save & Exit",True,Graphics.color_white)
	)

	#Name of the setting, the options, the current option value, and the function to execute on change
	menu_items = [
		["Window",["Small","Medium","Large"],0,"SetResolution"], #Resolution and size of the game window
		["Sound",["Off","On"],1,"SetSound"], #On/Off (volume muting) for all game sounds
		["Music",["Off","On"],1,"SetMusic"], #On/Off (volume muting) for the streamed music
		["Difficulty",["Easy","Normal","Crazy"],1,"SetDifficulty"], #Determines the grid size (20x40,10x20,5x10)
		["Style",["Squares","Circles"],0,"SetStyle"], #What the grid cells look like
		["Colors",["1","2","3","?"],0,"SetColors"], #Colors of the pieces (standard,odd,monochrome,nes tetris)
		["Mirrored",["No","Yes"],0,"SetMirrored"], #Whether the board and hud sides should be swapped
		["Guides",["No","Yes"],1,"SetGuides"], #Render ghost pieces
		["Sandwich",["Yes","No","Vegan"],0,"SetSandwich"] #<Insert Heavy Weapons Guy joke here>
	]
	menu_selection = 0

	#Called when a setting is changed from one of the "Set" functions - maintains consistency
	@classmethod
	def __UpdateSetting(cls,thisfunc="",val=0):
		for setting in cls.menu_items:
			if thisfunc in setting:
				setting[2] = val
				return setting[1][val]

	#Called by the user to execute the changed setting and set the change
	@classmethod
	def UpdateSettings(cls,item):
		getattr(cls,cls.menu_items[item][3])(cls.menu_items[item][2])
	
	#Load saved settings from JSON file in assets folder - called on start of program
	@classmethod
	def LoadSettings(cls):
		#Check if a settings file already exists, but don't create one
		data = FileData(cls.settings_file_name,"r",create_file=False)
		
		if not data:
			#No file - create one with default settings
			cls.SaveSettings()
			return
		
		#Look through loaded data and update the settings in the game to reflect the saved versions
		for k,v in data.items():
			for item in cls.menu_items:
				if k in item[0]:
					item[2] = item[1].index(v)
					cls.UpdateSettings(cls.menu_items.index(item))
		
		#Success
		print("Game settings loaded and applied")
		cls.settings_loaded = True
	
	#Save current settings to a JSON file in assets folder - called when exiting the settings menu
	@classmethod
	def SaveSettings(cls):
		output = {}
		for item in cls.menu_items:
			output.update({item[0]:item[1][item[2]]})
		FileData(cls.settings_file_name,"w",output)
	
	#Delete settings file
	@classmethod
	def DeleteSettings(cls):
		return FileData(cls.settings_file_name,delete_file=True)
	
	#All functions called from "ChangeSetting" or when settings are loaded on start
	@classmethod
	def SetResolution(cls,val=0):
		new_setting = cls.__UpdateSetting("SetResolution",val)
		print(f"Resolution is: {new_setting}")
		global GAME_WINDOW,SCREEN_WIDTH,SCREEN_HEIGHT
		r = Graphics.resolutions[val]
		SCREEN_WIDTH,SCREEN_HEIGHT = r,r
		GAME_WINDOW = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
	
	@classmethod
	def SetSound(cls,val=0):
		new_setting = cls.__UpdateSetting("SetSound",val)
		print(f"Sound is: {new_setting}")
		Audio.Volume(val,change_music=False)
	
	@classmethod
	def SetMusic(cls,val=0):
		new_setting = cls.__UpdateSetting("SetMusic",val)
		print(f"Music is: {new_setting}")
		Audio.Volume(val,change_sound=False)
	
	@classmethod
	def SetDifficulty(cls,val=0):
		new_setting = cls.__UpdateSetting("SetDifficulty",val)
		print(f"Difficulty is: {new_setting}")
		Gameplay.saved_difficulty = val
		#Reset the game on difficulty change, only if the player hasn't really played the current game
		if cls.settings_loaded and Score.current_score == 0:SetupGame()
	
	@classmethod
	def SetStyle(cls,val=0):
		new_setting = cls.__UpdateSetting("SetStyle",val)
		print(f"Style is: {new_setting}")
		Graphics.grid_style = val
	
	@classmethod
	def SetColors(cls,val=0):
		new_setting = cls.__UpdateSetting("SetColors",val)
		print(f"Colors is: {new_setting}")
		UpdateColors(val)
	
	@classmethod
	def SetMirrored(cls,val=0):
		new_setting = cls.__UpdateSetting("SetMirrored",val)
		print(f"Mirrored is: {new_setting}")
		Graphics.window_mirror = bool(val)
	
	@classmethod
	def SetGuides(cls,val=0):
		new_setting = cls.__UpdateSetting("SetGuides",val)
		print(f"Guides is: {new_setting}")
		Gameplay.ghost_tetromino_active = bool(val)
	
	@classmethod
	def SetSandwich(cls,val=0):
		new_setting = cls.__UpdateSetting("SetSandwich",val)
		print(f"Sandwich is: {new_setting}")
		if val == 0:print("Sandwich is good...")
		if val == 1:print("You will go hungry without sandwich...")
		if val == 2:print("Not really a sandwich is it?")
print("Classes loaded")

#-----Game state functions
def SetupGame():
	"""Called to start a new round of Tetris - also called at initialize to setup the game for the first time"""
	
	#Pause game until user is ready to play
	PauseGame()
	
	#Reset/initialize the game so user can play a new round
	Gameplay.gameover_active = False
	Gameplay.gameover_screen_active = False
	Gameplay.panic_active = False
	Board.coords = [0,0]
	Score.current_score = 0
	Score.cleared_lines = 0
	ChangeLevel(reset=True)
	Gameplay.ghost_tetromino = None
	
	#Handle new difficulty settings (if changed)
	Gameplay.game_difficulty = Gameplay.saved_difficulty
	if Gameplay.game_difficulty == 0: Board.size_x,Board.size_y = 20,40
	if Gameplay.game_difficulty == 1: Board.size_x,Board.size_y = 10,20
	if Gameplay.game_difficulty == 2: Board.size_x,Board.size_y = 5,10
	
	#Set board and spawn the first tetromino
	CalculateBoard(True)
	SpawnPiece()
	
	#Load music
	Audio.LoadMusic(assets["main_theme"])
def GameOver():
	"""Called when player triggers game over - stops gameplay, saves scores, and makes game over the active state"""
	print("Finished")
	
	#Stop gameplay and save the score to the scores list if high enough
	Gameplay.gameover_active = True
	Gameplay.gameover_final_score = Score.SaveScore()
	if Gameplay.gameover_final_score:
		#Current score made it to the highscore list
		print("Made the highscore!")
	else:
		print("Didn't make the highscore.")
	Gameplay.gameover_highscores = Score.GetScores()

	#Stop and load new music and sounds and play some game over effects
	Audio.LoadMusic(assets["game_over_theme"])
	Audio.PlaySound(assets["game_over_effect"])

	#Show an overlay flash on the board
	Board.overlay_draw = True
	GameTimer.SetTimer("overlay_flash",0.25)

	#Time the board-falling to shortly begin when the game over sound finishes
	GameTimer.SetTimer("gameover_boardfall",assets["game_over_effect"].get_length()+1)
def PauseGame():
	"""Pause game if game wasn't already in that state. Affects the displaying of the pause screen."""
	if Gameplay.game_paused:return

	Gameplay.game_paused = True
	Gameplay.pause_screen_active = True
	Audio.Freeze() #Pause any current music and sounds coming from gameplay
def ResumeGame(countdown=True):
	"""Resume the game being played if game was paused.\n
	If countdown is false, the game will immediately resume without the countdown. If true, the game will still be paused (without pause screen or settings or controls active) and instead begin a countdown in place of the pause screen until the countdown ends.\n
	The countdown ending won't actually resume the game, instead this function must be called again as false at the conditional of when the timer stops."""
	if not Gameplay.game_paused:return

	#Called by this function to begin the countdown towards gameplay
	def StartCountdown():
		"""Start the game countdown whenever the game becomes unpaused and needs a countdown timer."""
		Gameplay.countdown_active = True
		Gameplay.countdown_current_time = Gameplay.countdown_timer
		GameTimer.RemoveTimer("game_countdown")
		GameTimer.SetTimer("game_countdown",Gameplay.countdown_speed,Gameplay.countdown_timer)
	
	#These should always be called when the game is resumed, regardless of countdown
	SettingsMenu(False)
	Gameplay.pause_screen_active = False

	#Resume was called with the countdown - ignore rest of function until called again without countdown
	if countdown:
		StartCountdown()
		return
	
	#Resume the game
	Gameplay.countdown_active = False
	Gameplay.game_paused = False
	Audio.Freeze(False)
def SettingsMenu(open_menu=True):
	"""Bring up settings menu (or close) if it wasn't already in that state"""
	
	if Settings.menu_active and open_menu:return
	elif not Settings.menu_active and not open_menu:return
	else:
		if open_menu:
			#Bringing up settings will pause the game
			PauseGame()
			Settings.menu_active = True
		else:
			#Write settings to file here
			Settings.SaveSettings()
			Settings.menu_active = False
def ChangeSetting(setting=0,option=0):
	"""Controlled by user to scroll up or down in the settings menu and change the options"""
	
	s = Settings.menu_selection
	
	#User is at top or bottom of setting list - do nothing
	if s+setting < 0 or s+setting >= len(Settings.menu_items):return
	
	#Scroll up or down the settings menu
	Settings.menu_selection += setting
	s = Settings.menu_selection
	o = Settings.menu_items[s][2]
	
	#User is at max left or right of the setting options - do nothing
	if o+option < 0 or o+option >= len(Settings.menu_items[s][1]):return
	
	#Scroll through the options on a setting
	Settings.menu_items[s][2] += option

	#User has changed a setting - execute the correct function to reflect changes
	if option != 0:
		Settings.UpdateSettings(s)
	
	Audio.PlaySound(assets["user_action"])
print("State loaded")

#-----Gameplay functions
def CalculateBoard(reset=False):
	"""Generate board with already locked cells minus the player's tetromino and ghost"""
	if not reset:
		for row in range(len(Board.grid)):
			for cell in range(len(Board.grid[0])):
				for x,y in Gameplay.prior_tetromino_coords:
					#Remove player tetromino so that only locked cells remain
					pos = (x,y)
					c = (cell,row)
					if c == pos:
						Board.grid[row][cell] = Board.color_empty

		#Calculate the ghost piece apart from the grid
		Gameplay.ghost_tetromino = CalculateGhostPiece()
	
	#Reset on start of game for a fresh board
	else:
		#Make an empty board containing an x by y grid list containing blank cells
		Board.grid = [[Board.color_empty for _ in range(Board.size_x)]for _ in range(Board.size_y)]
def GenerateRandomPiece(x=0,y=0):
	"""Return a randomly chosen tetris piece from a 'bag'"""
	
	#The bag is empty - make a new one containing each tetromino
	if not Gameplay.random_tetromino_bag:
		for _ in range(Gameplay.bag_piece_count):
			for i in range(len(Shapes.shapes)):
				Gameplay.random_tetromino_bag.append(Shapes.shapes[i])
	
	#Choose a piece randomly and remove it from the bag
	chosen_piece = Gameplay.random_tetromino_bag.pop(random.choice(range(len(Gameplay.random_tetromino_bag))))
	
	return Tetromino(x,y,chosen_piece)
def SpawnPiece():
	"""Instantiate a new piece from the spawn point"""
	
	#Get an initial piece
	if not Hud.next_tetromino:
		Hud.next_tetromino = GenerateRandomPiece()

	Gameplay.player_tetromino = Hud.next_tetromino
	Gameplay.player_tetromino.x,Gameplay.player_tetromino.y = 0,0

	xspawn = (Board.size_x//2) + Gameplay.piece_spawn_x
	yspawn = 0 + Gameplay.piece_spawn_y
	
	#"O" piece should be spawned one extra block to the side so it's centered
	op = (Gameplay.player_tetromino.shape == Shapes.shapes[2])
	Gameplay.player_tetromino.Move(xspawn+1 if op else xspawn,Gameplay.piece_spawn_y)
	
	#Get a new tetromino piece for the next time
	Hud.next_tetromino = GenerateRandomPiece()
	
	#Make sure the piece starts moving down once spawned
	Gameplay.piece_fall_active = True
def CalculateGhostPiece():
	if not Gameplay.player_tetromino:return
	else:ghost_piece = copy.deepcopy(Gameplay.player_tetromino)

	while True:
		ghost_piece.Move(0,1)
		if InvalidMove(ghost_piece):
			ghost_piece.Move(0,-1)
			break

	return ghost_piece
def ChangeLevel(level=1,reset=False):
	"""Changes the level, which changes the speed and other gameplay values"""
	
	Score.current_level = level
	gravity = 2 ** (level * Gameplay.level_speedup_factor) - 1
	Gameplay.piece_fall_speed = int(Gameplay.level_speedup_init + gravity)
	print(Gameplay.piece_fall_speed)

	#Level up effects
	if not reset:
		Audio.PlaySound(assets["level_increase"])
		Gameplay.level_flicker_active = True
		#Change colors of the board blocks and pieces if color setting is on random
		val = Settings.menu_items[5][2]
		if val == Settings.menu_items[5][1].index("?"):
			UpdateColors(val,True)
def ClearLines():
	"""Called when a piece gets locked to the board. Checks for any grid lines that are full and needing to be cleared. An animation plays that 'sweeps' the board using a secondary game loop while the rest of the game is frozen. After that, the score is calculated."""

	#Check for lines on the board that are filled up with blocks, remove them, and calculate score
	lines_cleared,clear_list = 0,[]
	
	#Loop through grid line-by-line to get filled rows
	for row in range(len(Board.grid)):
		
		#Focus on current line and check if it has no empty cells
		this_row = list(Board.grid[row])
		if Board.color_empty not in this_row:
			
			#This line is filled - loop through it and add the x/y to the line list
			clear_list.append(this_row)
			for cell in range(len(this_row)):
				c = (cell,row)
				clear_list[lines_cleared][cell] = c
			
			lines_cleared += 1
	
	#List has at least one row that needs clearing
	if clear_list:
		
		Audio.PlaySound(assets["score_line"])
		if lines_cleared >= 4:
			#Tetris clear!
			Audio.PlaySound(assets["score_tetris"])
			GameTimer.SetTimer("tetris_flicker",Gameplay.line_clear_flicker_speed,-1)
		
		#Animate the removal of the lines cell-by-cell
		current_column = 0
		GameTimer.SetTimer("clear_line",Gameplay.line_clear_speed,-1)

		#The main loop is paused so a temp running loop is necessary for animation
		while True:
			global DELTATIME,GAME_TIME
			DELTATIME = GAME_CLOCK.tick_busy_loop(FRAME_RATE) / 1000
			GAME_TIME += DELTATIME
			GameTimer.Update(GAME_TIME,DELTATIME)
			pygame.event.pump()
			events = pygame.event.get()

			#Listen for timers
			for e in events:
				if e.type == pygame.USEREVENT:
					
					#Animate away one cell of each row at a time over the course of a second
					if e.GameTimerEvent == "clear_line":
						cell_direction = 1 #Change cell removal direction on each row
						
						for r in clear_list:
							x = current_column*cell_direction
							y = r[0][1]
							if cell_direction == 1:Board.grid[y][x] = Board.color_empty
							else:Board.grid[y][x-1] = Board.color_empty
							cell_direction = -cell_direction
						
						current_column += 1
					
					if e.GameTimerEvent == "tetris_flicker":
						Graphics.window_flicker_effect = not Graphics.window_flicker_effect
			
			#Redraw necessary parts to show animations
			DrawWindow()
			DrawHud()
			DrawBoard(True,True)
			pygame.display.update()
			
			#Break loop when list is exhausted
			if current_column >= len(clear_list[0]):
				Graphics.window_flicker_effect = False
				break
			
		#Prevent events from stockpiling during this controless moment
		events.clear()
		
		#Clear the animation timers
		GameTimer.RemoveTimer("clear_line")
		GameTimer.RemoveTimer("tetris_flicker")

		#Start from bottom and remove rows from grid upward and then insert same number of empty rows from the top
		for empty_row in range(len(clear_list)-1,-1,-1):
			y = clear_list[empty_row][0][1]
			del Board.grid[y]
		for empty_row in range(len(clear_list)):
			Board.grid.insert(0,[Board.color_empty for _ in Board.grid[1]])
		
		#Handle scoring, cleared lines, and level ups
		Score.current_score += (Score.line_scores[lines_cleared-1]*Score.current_level)
		Score.cleared_lines += lines_cleared
		
		#Increase level by one every time a certain number of lines gets cleared
		if int(Score.cleared_lines/Gameplay.level_threshold) >= Score.current_level:
			ChangeLevel(Score.current_level+1)
def InvalidMove(piece):
	"""Checks if the player or ghost tetromino is out of bounds or is intersecting with a locked cell"""
	
	#Get a list of all empty cells on the board
	empty_cells = [[(column, row) for column in range(len(Board.grid[0])) if Board.grid[row][column] == Board.color_empty] for row in range(len(Board.grid))]
	
	#Arrange them to be a grid of x/y cells
	empty_cells = [column for sub in empty_cells for column in sub]
	
	#Get piece coordinates and see if a block is not in an open cell
	for pos in piece.block_positions:
		
		#Make sure piece wont get stuck in top left/right corners of grid
		if pos[0] < 0 or pos[0] >= len(Board.grid[0]):
			return True
		
		if pos not in empty_cells:
			#Its okay for piece to be out of bounds above grid
			if pos[1] >= 0:
				return True
	
	#All good - no collisions
	return False
def MovePiece(x=0,y=0):
	"""Move the active piece a number of units along the grid, with respect to collisions."""

	#Try to move piece along grid
	Gameplay.player_tetromino.Move(x,y)
	
	#Cant move - return to original position
	if InvalidMove(Gameplay.player_tetromino):
		Gameplay.player_tetromino.Move(-x,-y)
		return False
	
	#Move successful
	return True
def RotatePiece(clockwise=True):
	"""Rotate the active piece in place, with respect to collisions. Uses a 'kick' feature that prevents piece from getting stuck or unable to rotate when it should."""
	
	#Try to rotate piece
	Gameplay.player_tetromino.Rotate(clockwise)
	
	#Cant rotate - return to original rotation
	if not KickPiece():
		Gameplay.player_tetromino.Rotate(not clockwise)
		return False
	
	#Rotation successful
	return True
def KickPiece():
	"""Help the piece by trying to move it outside of a collision so it can rotate more fluidly"""
	
	#"O" piece can rotate all it wants
	if Gameplay.player_tetromino.shape == Shapes.shapes[2]:
		return True
	
	#Piece can rotate just fine without any help
	if not InvalidMove(Gameplay.player_tetromino):
		return True
	
	#Piece needs some help
	else:
		moves = [[-1,0],[1,0],[0,1],[0,-1],[-1,1],[1,1],[-1,-1],[1,-1]]
		
		#"I" piece may need to move in a direction twice since its 4 blocks long
		#All other pieces need only move once in a direction, otherwise the rotation was doomed to fail regardless - and anything else is basically cheating
		if Gameplay.player_tetromino.shape == Shapes.shapes[4]:
			extra_moves = [[-2,0],[2,0],[0,2],[0,-2],[-2,2],[2,2],[-2,-2],[2,-2]]
			moves.extend(extra_moves)
		
		for x,y in moves:
			
			#Try to move the piece in a direction
			Gameplay.player_tetromino.Move(x,y)
			
			#Not working - put the piece back
			if InvalidMove(Gameplay.player_tetromino):
				Gameplay.player_tetromino.Move(-x,-y)
			
			#It worked - piece fits
			else:
				return True
	
	#Piece cannot rotate without collision
	return False
def DropPiece():
	"""Cause the player piece to instantly drop to whatever is directly below it"""
	
	while True:
		
		#Move piece downward indefinitely until it hits something below
		if MovePiece(0,1):
			#Update score a certain amount of points per cell
			Score.current_score += Score.drop_points
		
		else:
			break
	
	#Piece has hit whatever was below - lock the piece immediately
	LockPiece()
def LockPiece():
	"""Lock the players tetromino to the board"""

	#Look through the grid and find where the tetromino is and render those cells with its color
	for row in range(len(Board.grid)):
		for cell in range(len(Board.grid[0])):
			for x,y in Gameplay.player_tetromino.block_positions:
				
				pos = (x,y)
				c = (cell,row)
				
				if c == pos:
					Board.grid[row][cell] = Gameplay.player_tetromino.color
	
	#Play lock sound
	Audio.PlaySound(assets["piece_lock"])
	
	#Check for any lines that need to be cleared and then spawn the next piece
	ClearLines()
	SpawnPiece()

	#Check if panic time
	CheckPanic()
def CheckPanic():
	try:
		trigger_row = round((Board.size_y / Gameplay.panic_grid_threshold)+0.5) - 1
		threshold_met = True if any([i for i in Board.grid[trigger_row] if i != Board.color_empty]) else False
	except IndexError or ZeroDivisionError:return
	if threshold_met and not Gameplay.panic_active:
		Audio.LoadMusic(assets["main_theme_fast"])
		Audio.PlayMusic()
		Gameplay.panic_active = True
	if not threshold_met and Gameplay.panic_active:
		Audio.LoadMusic(assets["main_theme"])
		Audio.PlayMusic()
		Gameplay.panic_active = False
print("Gameplay loaded")

#-----Graphics functions
def UpdateColors(setting=0,override=False):
	"""Called from color setting to change the color palette of the tetris shapes as they get newly spawned\n
	'override' will immediately change the shape colors as well as piece colors that have spawned and lie on the grid"""
	
	color_set_1 = [
		Graphics.color_red,
		Graphics.color_orange,
		Graphics.color_yellow,
		Graphics.color_green,
		Graphics.color_cyan,
		Graphics.color_blue,
		Graphics.color_purple
	]
	color_set_2 = [
		Graphics.color_sea,
		Graphics.color_chocolate,
		Graphics.color_spring,
		Graphics.color_magenta,
		Graphics.color_olive,
		Graphics.color_salmon,
		Graphics.color_teal
	]

	current_color_set = [s[0] for s in Shapes.shapes]

	if setting == 0:
		#Standard
		new_color_set = color_set_1
	elif setting == 1:
		#Odd
		new_color_set = color_set_2
	elif setting == 2:
		#Monochrome (technically complementary)
		c = tuple(map(lambda c1,c2:c1-c2,Graphics.color_white,Board.color_empty))
		new_color_set = [c] * 7
	elif setting == 3:
		#Nes Tetris!
		def rand_color():
			c = pygame.Color(0,0,0)
			c.hsva = (random.randint(0,360),random.randint(75,100),random.randint(75,100))
			return (c[0],c[1],c[2])
		r1 = rand_color()
		r2 = rand_color()
		new_color_set = [r1,r2,Graphics.color_white,r2,Graphics.color_white,r1,Graphics.color_white]

	#Change colors for active and set pieces OR just the upcoming pieces	
	for i,shape in enumerate(Shapes.shapes):
		shape[0] = new_color_set[i]
	if not override:return
	else:
		#Grid color update
		for row in range(len(Board.grid)):
			for cell in range(len(Board.grid[0])):
				for i,color in enumerate(current_color_set):
					if Board.grid[row][cell] == color:
						Board.grid[row][cell] = new_color_set[i]
		#Player piece and next tetromino color update
		Gameplay.player_tetromino.color = Gameplay.player_tetromino.shape[0]
		Hud.next_tetromino.color = Hud.next_tetromino.shape[0]
def DrawWindow():
	"""Draws background and arranges left and right halves of it's playing areas"""

	#Draw window background as one color or another
	bg_color = Graphics.color_black
	if Graphics.window_flicker_effect:bg_color = Graphics.color_white
	GAME_WINDOW.fill(bg_color)
	
	#Handle mirroring of the board and hud sections
	left = (0,0) if not Graphics.window_mirror else (SCREEN_WIDTH//2,0)
	right = (0,0) if Graphics.window_mirror else (SCREEN_WIDTH//2,0)
	Graphics.window_half_coord1,Graphics.window_half_coord2 = left,right
def DrawBoard(exclude_player_piece=False,exclude_ghost_piece=False):
	"""Draws everything related to the Tetris game board - grid, cells, player piece, ghost piece, etc"""
	
	Board.coords[0] = Graphics.window_half_coord1[0]
	Board.width,Board.height = SCREEN_WIDTH//2,SCREEN_HEIGHT #Update size of board

	#Add in the player piece to the grid, but keep a copy of its coordinates so it can be removed and re-added on the next loop (prevents collision issues with itself)
	if not exclude_player_piece:
		Gameplay.prior_tetromino_coords = list(Gameplay.player_tetromino.block_positions)
		for x,y in Gameplay.player_tetromino.block_positions:
			#Only draw if piece is inside the board, otherwise game will crash
			if y >= 0:
				Board.grid[y][x] = Gameplay.player_tetromino.color
	
	#Final cell unit drawing
	cell_size_x = Board.width/Board.size_x
	cell_size_y = Board.height/Board.size_y
	for row in range(len(Board.grid)):
		for column in range(len(Board.grid[row])):
			x = int(Board.coords[0] + column*cell_size_x)
			y = int(Board.coords[1] + row*cell_size_y)

			#Draw player tetromino blocks
			if Graphics.grid_style == 0: #Squares
				pygame.draw.rect(GAME_WINDOW,Board.grid[row][column],pygame.Rect(x,y,int(cell_size_x),int(cell_size_y)))
			elif Graphics.grid_style == 1: #Circles
				pygame.draw.ellipse(GAME_WINDOW,Board.grid[row][column],pygame.Rect(x,y,int(cell_size_x),int(cell_size_y)))
			
			#Draw ghost blocks seperate from the grid
			if not exclude_ghost_piece and Gameplay.ghost_tetromino_active:
				if Gameplay.ghost_tetromino:
					for gx,gy in Gameplay.ghost_tetromino.block_positions:
						pos = (gx,gy)
						c = (column,row)
						if c == pos:
							if Graphics.grid_style == 0: #Squares
								pygame.draw.rect(GAME_WINDOW,Gameplay.ghost_tetromino.color,pygame.Rect(x,y,int(cell_size_x),int(cell_size_y)),2)
							elif Graphics.grid_style == 1: #Circles
								pygame.draw.ellipse(GAME_WINDOW,Gameplay.ghost_tetromino.color,pygame.Rect(x,y,int(cell_size_x),int(cell_size_y)),2)
	
	#Loop through drawing the grid edges line by line left-right top-bottom
	if Graphics.grid_style == 0: #Only draw if square style
		for column_lines in range(len(Board.grid[0])):
			sx = int(Board.coords[0] + column_lines*cell_size_x)
			sy = int(Board.coords[1])
			ex = int(Board.coords[0] + column_lines*cell_size_x)
			ey = int(Board.coords[1] + Board.height)
			pygame.draw.line(GAME_WINDOW,Board.color_gridlines,(sx,sy),(ex,ey))
		for row_lines in range(len(Board.grid)):
			sx = int(Board.coords[0])
			sy = int(Board.coords[1] + row_lines*cell_size_y)
			ex = int(Board.coords[0] + Board.width)
			ey = int(Board.coords[1] + row_lines*cell_size_y)
			pygame.draw.line(GAME_WINDOW,Board.color_gridlines,(sx,sy),(ex,ey))
	
	#Draw an outline from top-left to bottom-right of the board
	outline = pygame.Rect(Board.coords[0],Board.coords[1],Board.width,Board.height)
	pygame.draw.rect(GAME_WINDOW,Board.color_outline,outline,Board.outline_width)

	#Draw an overlay on the board if active
	if Board.overlay_draw:
		overlay = pygame.Rect(Board.coords[0],Board.coords[1],Board.width,Board.height)
		pygame.draw.rect(GAME_WINDOW,Board.overlay_color,overlay)
def DrawHud():
	"""Draws the heads up display for the player"""
	
	Hud.coord[0] = Graphics.window_half_coord2[0]
	Hud.height,Hud.width = SCREEN_HEIGHT,SCREEN_WIDTH//2 #Update size of hud
	area = pygame.Rect(Hud.coord[0],Hud.coord[1],Hud.width,Hud.height) #Create rect coords for whole hud
	
	#Divide hud area into 4 stacked sections containing the content
	sections = [0 for _ in range(4)]
	section_offset = 20

	#Title
	size_title = Hud.title.get_rect()
	title = GAME_WINDOW.blit(Hud.title,(area.centerx-size_title.centerx,sections[0]))

	#Next piece window
	sections[1] = title.bottom + section_offset
	outline_centerx = Hud.nextpiece_window_size[0]//2
	outline = pygame.Rect(area.centerx-outline_centerx,sections[1],Hud.nextpiece_window_size[0],Hud.nextpiece_window_size[1])
	pygame.draw.rect(GAME_WINDOW,Hud.nextpiece_window_color,outline,Hud.nextpiece_window_width)
	size_nextpiece = Hud.nextpiece_text.get_rect()
	next_win = GAME_WINDOW.blit(Hud.nextpiece_text,(outline.centerx-size_nextpiece.centerx,outline.bottom+5))
	
	#Next piece
	blocks = Hud.next_tetromino.block_positions
	ps = Hud.nextpiece_block_size #size of blocks in pixels
	offset_x = (max(x[0] for x in blocks)+1)/2
	offset_y = (max(y[1] for y in blocks)+1)/2
	for pos in range(len(blocks)):
		px = int(outline.centerx + (blocks[pos][0]-offset_x)*ps)
		py = int(outline.centery + (blocks[pos][1]-offset_y)*ps)

		#Draw style
		if Graphics.grid_style == 0: #Squares
			pygame.draw.rect(GAME_WINDOW,(Hud.next_tetromino.color),pygame.Rect(px,py,ps,ps))
		elif Graphics.grid_style == 1: #Circles
			pygame.draw.ellipse(GAME_WINDOW,(Hud.next_tetromino.color),pygame.Rect(px,py,ps,ps))
	
	#Score
	sections[2] = next_win.bottom + section_offset
	
	#Show current score and lines
	Hud.score_text_points = Graphics.font_mid.render(f"Score: {Score.current_score:,}",True,Graphics.color_white)
	Hud.score_text_lines = Graphics.font_mid.render(f"Lines: {Score.cleared_lines}",True,Graphics.color_white)
	#Flicker effect for level information on level change
	txt_level_color = Graphics.color_white if not Gameplay.level_flicker_toggle else Graphics.color_black
	if Gameplay.level_flicker_active:
		if GameTimer.SetTimer("level_flicker",Gameplay.level_flicker_speed,Gameplay.level_flicker_intervals):
			Gameplay.level_flicker_toggle = not Gameplay.level_flicker_toggle
		if GameTimer.SetTimer("level_flicker_cutoff",Gameplay.level_flicker_intervals):
			Gameplay.level_flicker_active = False
			Gameplay.level_flicker_toggle = False
			GameTimer.RemoveTimer("level_flicker")
			GameTimer.RemoveTimer("level_flicker_cutoff")
			txt_level_color = Graphics.color_white
	Hud.score_text_level = Graphics.font_mid.render(f"Level: {Score.current_level}",True,txt_level_color)
	#Text rects
	size_score = Hud.score_text_points.get_rect()
	size_lines = Hud.score_text_lines.get_rect()
	size_level = Hud.score_text_level.get_rect()
	
	#Draw score information text
	score = GAME_WINDOW.blit(Hud.score_text_points,(area.centerx-size_score.centerx,sections[2]))
	lines = GAME_WINDOW.blit(Hud.score_text_lines,(area.centerx-size_lines.centerx,sections[2]+30))
	level = GAME_WINDOW.blit(Hud.score_text_level,(area.centerx-size_level.centerx,sections[2]+60))

	#Controls - depending on gameover or not
	sections[3] = level.bottom + section_offset
	size_ctrl_title = Hud.controls_title.get_rect()
	ctrl_title = GAME_WINDOW.blit(Hud.controls_title,(area.centerx-size_ctrl_title.centerx,sections[3]))
	offset = 0
	for txt in Hud.controls_text[0 if not Gameplay.gameover_active else 1]:
		size_control = txt.get_rect()
		txt_offset = ctrl_title.bottom + 5
		txt_line = GAME_WINDOW.blit(txt,(area.centerx-size_control.centerx,txt_offset+(25*offset)))
		offset += 1
def DrawPause():
	"""Draw pause screen over the game board"""
	
	#Create and draw a transparent background
	surf = pygame.Surface((Board.width,Board.height))
	surf.fill(tuple(Graphics.trans_surf[0:3]))
	surf.set_alpha(Graphics.trans_surf[3])
	area = GAME_WINDOW.blit(surf,(Board.coords[0],Board.coords[1]))#Background
	
	#Screen area info text handling
	offsets = (200,10,50,5,20,5,50)
	prev_txt_bottom = 0
	
	for txt in range(len(Gameplay.pause_text)):
		txt_size = Gameplay.pause_text[txt].get_rect()
		
		if txt == 0:
			txt_surf = GAME_WINDOW.blit(Gameplay.pause_text[txt],(area.centerx-txt_size.centerx,area.centery-offsets[txt]))
		else:
			txt_surf = GAME_WINDOW.blit(Gameplay.pause_text[txt],(area.centerx-txt_size.centerx,prev_txt_bottom+offsets[txt]))
		
		prev_txt_bottom = txt_surf.bottom
def DrawCountdown():
	"""Draw the countdown timer number"""
	area = pygame.Rect(Board.coords[0],Board.coords[1],Board.width,Board.height)
	txt = Graphics.font_yuge.render(str(Gameplay.countdown_current_time),True,Gameplay.countdown_text_color)
	size_txt = txt.get_rect()
	txt_surf = GAME_WINDOW.blit(txt,(area.centerx - size_txt.centerx,area.centery - size_txt.centery))
def DrawGameOver():
	"""Draw the game over screen over where the game board would be"""
	
	area = pygame.Rect((Graphics.window_half_coord1),(SCREEN_WIDTH//2,SCREEN_HEIGHT))

	#Size the background image and draw it so it covers whole game over screen half
	bg_img = pygame.transform.smoothscale(assets["game_over_background"],(area.size[0],area.size[1]))
	size_bg = bg_img.get_rect()
	background = GAME_WINDOW.blit(bg_img,(area.left,area.top))

	#Render title
	size_title = Gameplay.gameover_text_title.get_rect()
	title = GAME_WINDOW.blit(Gameplay.gameover_text_title,(area.centerx-size_title.centerx,area.top+10))

	#Render highscore title
	size_hst = Gameplay.gameover_text_highscore.get_rect()
	hst = GAME_WINDOW.blit(Gameplay.gameover_text_highscore,(area.centerx-size_hst.centerx,title.bottom+10))

	#Render scores
	init_offset = True
	prev_txt_bottom = 0
	side_l = title.left
	side_r = title.right
	identical_score = False
	for rank,score in Gameplay.gameover_highscores.items():
		#Check if this is the score the player got
		current_color = Gameplay.gameover_text_color
		if Gameplay.gameover_final_score == score:
			#Check if this is the first instance of the player's score on the highscore list and not some duplicate further down
			if not identical_score:
				#Create an interval flickering effect for the player's score
				if GameTimer.SetTimer("score_flicker",0.5,-1):
					Gameplay.gameover_text_flicker = not Gameplay.gameover_text_flicker
				if Gameplay.gameover_text_flicker:current_color = Gameplay.gameover_text_color
				else:current_color = Graphics.color_white
				identical_score = True
		
		#Determine offset from other text elements if first score on the list
		if init_offset:
			offset = 3
			prev_txt_bottom = hst.bottom
		else:offset = 5

		#Score parts
		txt_num = Graphics.font_small.render(f"{rank}",True,current_color)
		txt_dif = Graphics.font_small.render(f"{Settings.menu_items[3][1][score[0]]}",True,current_color)
		txt_lines = Graphics.font_small.render(f"{score[1]}",True,current_color)
		txt_points = Graphics.font_small.render(f"{score[2]:,}",True,current_color)

		#Arrange them along a line
		num = GAME_WINDOW.blit(txt_num,(side_l,prev_txt_bottom+offset))
		dif = GAME_WINDOW.blit(txt_dif,(num.right+10,prev_txt_bottom+offset))
		lines = GAME_WINDOW.blit(txt_lines,(area.centerx-txt_lines.get_rect().centerx,prev_txt_bottom+offset))
		points = GAME_WINDOW.blit(txt_points,(side_r-txt_points.get_rect().right,prev_txt_bottom+offset))

		prev_txt_bottom = dif.bottom
		init_offset = False

	#Render replay text
	size_replay = Gameplay.gameover_text_replay.get_rect()
	replay = GAME_WINDOW.blit(Gameplay.gameover_text_replay,(area.centerx-size_replay.centerx,area.centery-10))
def DrawSettings():
	"""Draws the settings menu over the HUD"""
	
	area = pygame.draw.rect(GAME_WINDOW,Settings.menu_background_color,pygame.Rect(Hud.coord[0],Hud.coord[1],Hud.width,Hud.height))
	offset = 5
	offset_edges = 5
	
	#Title
	title_size = Settings.menu_title.get_rect()
	title = GAME_WINDOW.blit(Settings.menu_title,(area.centerx-title_size.centerx,area.top+offset))
	
	#Settings
	prev_txt_bottom = title.bottom+(offset*2)
	selected_setting = Settings.menu_selection
	
	#Render the selected setting
	for i,setting in enumerate(Settings.menu_items):
		stxt = Graphics.font_small.render(setting[0]+":",True,Settings.menu_color_setting)
		stxt_size = stxt.get_rect()
		setting_text = GAME_WINDOW.blit(stxt,(area.left+offset_edges,prev_txt_bottom+offset))
		
		#Render the options of the setting
		prev_txt_side = area.right
		init_offset = offset_edges
		for option in reversed(setting[1]):
			j = setting[1].index(option)
			txt_color = Settings.menu_color_items
			
			#Color all options the same except for the current selected value
			if i == selected_setting:
				if j == setting[2]:
					txt_color = Settings.menu_color_highlight
			
			vtxt = Graphics.font_small.render(" "+option,True,txt_color)
			vtxt_size = vtxt.get_rect()
			option_text = GAME_WINDOW.blit(vtxt,(prev_txt_side-vtxt_size.right-init_offset,prev_txt_bottom+offset))
			prev_txt_side = option_text.left
			init_offset = 0
		
		prev_txt_bottom = setting_text.bottom
	
	#Controls
	prev_ctrl_top = area.bottom-offset_edges
	for ctrl in reversed(Settings.menu_controls):
		ctrl_size = ctrl.get_rect()
		ctrl_text = GAME_WINDOW.blit(ctrl,(area.centerx-ctrl_size.centerx,prev_ctrl_top-ctrl_size.bottom-offset))
		prev_ctrl_top = ctrl_text.top
	
	size_ctrl_title = Settings.menu_title_controls.get_rect()
	ctrl_title = GAME_WINDOW.blit(Settings.menu_title_controls,(area.centerx-size_ctrl_title.centerx,prev_ctrl_top-(offset*10)))
def DrawFPS():
	"""Draw a window in the top-left of the screen showing current framerate. Activated in Graphics class."""
	r = pygame.draw.rect(GAME_WINDOW,Graphics.color_black,pygame.Rect(0,0,40,30))
	f = pygame.font.Font(assets["font_roboto"],12).render(str(int(GAME_CLOCK.get_fps())),False,Graphics.color_white)
	GAME_WINDOW.blit(f,(r.centerx-f.get_rect().centerx,r.centery-f.get_rect().centery))
print("Graphics loaded")

#-----Initialize game and settings
Settings.LoadSettings()
SetupGame()
print("Game initialized")

#-----Game engine loop
while RUNTIME:
	"""Main loop that runs at the framerate with realtime events"""
	
	#Engine runtime at frames per second
	DELTATIME = GAME_CLOCK.tick_busy_loop(FRAME_RATE) / 1000
	GAME_TIME += DELTATIME

	#Get all current engine events
	GameTimer.Update(GAME_TIME,DELTATIME)
	pygame.event.pump()
	events = pygame.event.get()

	"""Program and game state handling"""

	#Frozen state of the engine for when program is unfocused
	while FROZEN:
		DELTATIME = GAME_CLOCK.tick_busy_loop(FRAME_RATE) / 1000
		pygame.event.pump()
		events = pygame.event.get()
		for e in events:
			if e.type == pygame.ACTIVEEVENT:
				if e.state == 2 or e.state == 6:
					if e.gain == 1:
						FROZEN = False
		events.clear()

	#Top-level events and controls
	for e in events:
		#Render optional framerate
		if e.type == pygame.KEYDOWN and e.key == pygame.K_f:
			Graphics.render_fps = not Graphics.render_fps
		
		#Freeze when lost input focus on window
		if not pygame.key.get_focused():
			#Freeze engine until focus comes back
			FROZEN = True

			#If the user was playing, pause the game as well
			if not Gameplay.game_paused or not Gameplay.gameover_active:
				PauseGame()
		
		#Kill engine if user wants to quit
		if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
			RUNTIME = False
	
	#Game is paused and awaiting user interaction
	if Gameplay.game_paused and not Gameplay.countdown_active:
		
		#Events and controls while paused
		for e in events:
			if e.type == pygame.KEYDOWN:

				#Start the game
				if e.key == pygame.K_SPACE:
					#Start countdown timer, close pause screen and settings menu if open
					ResumeGame()
					Audio.PlaySound(assets["user_action"])
				
				#Toggle settings menu while paused
				if e.key == pygame.K_s:
					if Settings.menu_active:SettingsMenu(False)
					else:SettingsMenu()
				
					Audio.PlaySound(assets["user_action"])

				#Reset game
				if e.key == pygame.K_r:
					SetupGame()
					Audio.PlaySound(assets["user_action"])
		
		#Events and controls specific to the settings menu
		if Settings.menu_active:
			for e in events:
				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_UP:
						ChangeSetting(-1,0)
					if e.key == pygame.K_DOWN:
						ChangeSetting(1,0)
					if e.key == pygame.K_LEFT:
						ChangeSetting(0,-1)
					if e.key == pygame.K_RIGHT:
						ChangeSetting(0,1)
		
		#Clear pause events so they don't 'bleed' into other states
		events.clear()

	#Game is counting down till unpause
	if Gameplay.countdown_active:
		for e in events:
			if e.type == pygame.USEREVENT and e.GameTimerEvent == "game_countdown":
				Gameplay.countdown_current_time -= 1
				if Gameplay.countdown_current_time <= 0:
					ResumeGame(False)

	#Game is now over
	if Gameplay.gameover_active:

		#Listen for action and user input events
		for e in events:

			#Timed events
			if e.type == pygame.USEREVENT:

				#Flash the board with the overlay effect
				if e.GameTimerEvent == "overlay_flash":
					GameTimer.RemoveTimer("overlay_flash")
					Board.overlay_draw = False

				#Drop the board
				if e.GameTimerEvent == "gameover_boardfall":
					GameTimer.RemoveTimer("gameover_boardfall")
					Gameplay.gameover_board_drop = True
					Audio.PlaySound(assets["board_fall"])

				#Show game over screen and play music
				if e.GameTimerEvent == "gameover_screen":
					GameTimer.RemoveTimer("gameover_screen")
					print("Game Over")
					Audio.PlayMusic()
					Gameplay.gameover_screen_active = True

			#Game over screen is active
			if Gameplay.gameover_screen_active:

				#Listen for player choice input
				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_y:
						SetupGame() #Start a new game
						Audio.PlaySound(assets["user_action"])
					if e.key == pygame.K_n:RUNTIME = False #Quit the game

		#Drop the board off the screen
		if Gameplay.gameover_board_drop:

			#Accelerate the board downwards
			Gameplay.gameover_board_speed += (Gameplay.gameover_board_speed * Gameplay.gameover_board_accel) * DELTATIME
			Board.coords[1] = int(Gameplay.gameover_board_speed)

			#Check if board is offscreen and begin the game over sequence
			if Board.coords[1] > SCREEN_HEIGHT*2:
				Gameplay.gameover_board_speed = 1
				Gameplay.gameover_board_drop = False
				GameTimer.SetTimer("gameover_screen",assets["board_fall"].get_length()+1)

	#Run game of Tetris as long as it isn't frozen by pause, game over, or countdown
	if not Gameplay.game_paused and not Gameplay.countdown_active and not Gameplay.gameover_active:
		CalculateBoard()
		
		#Handle playing input
		pressed_keys = pygame.key.get_pressed()
		for e in events:
			
			"""Single-fire input"""
			if e.type == pygame.KEYDOWN:
				
				#Rotate piece clockwise
				if e.key == pygame.K_UP:
					if RotatePiece(True):
						Audio.PlaySound(assets["piece_rotate"])
				
				#Rotate piece anti-clockwise
				if e.key == pygame.K_z:
					if RotatePiece(False):
						Audio.PlaySound(assets["piece_rotate"])
				
				#Move piece left once
				if e.key == pygame.K_LEFT:
					if MovePiece(-1,0):
						Audio.PlaySound(assets["piece_move"])
				
				#Move piece right once
				if e.key == pygame.K_RIGHT:
					if MovePiece(1,0):
						Audio.PlaySound(assets["piece_move"])
				
				#Drop piece immediately
				if e.key == pygame.K_SPACE:
					DropPiece()
				
				#Pause game
				if e.key == pygame.K_RETURN:
					PauseGame()
					Audio.PlaySound(assets["user_action"])
				
				#Reset game
				if e.key == pygame.K_r:
					SetupGame()
					Audio.PlaySound(assets["user_action"])
				
				#Bring up settings
				if e.key == pygame.K_s:
					SettingsMenu()
					Audio.PlaySound(assets["user_action"])
			
			"""Keys that are released"""
			if e.type == pygame.KEYUP:

				if e.key == pygame.K_DOWN or e.key == pygame.K_RETURN or e.key == pygame.K_SPACE:
					#Hacky helper
					Gameplay.piece_fall_active = True
				
				if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
					GameTimer.RemoveTimer("move_sides_held")
					Gameplay.piece_horizontal_repeat_active = False
			
			"""Repeating-fire input"""
			if pressed_keys and e.type == pygame.USEREVENT:
				#Timers for piece moving repeatedly
				GameTimer.SetTimer("move_sides_repeat",1/Gameplay.piece_horizontal_speed,-1)
				GameTimer.SetTimer("move_down_repeat",1/(Gameplay.piece_vertical_speed+Gameplay.piece_fall_speed),-1)
				GameTimer.SetTimer("piece_fall",1/Gameplay.piece_fall_speed,-1)
				
				#Move piece left or right repeatedly
				if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_RIGHT]:
					if GameTimer.SetTimer("move_sides_held",Gameplay.piece_horizontal_delay):
						Gameplay.piece_horizontal_repeat_active = True
					if e.GameTimerEvent == "move_sides_repeat" and Gameplay.piece_horizontal_repeat_active:
						if pressed_keys[pygame.K_LEFT]:
							if MovePiece(-1,0):
								Audio.PlaySound(assets["piece_move"])
						if pressed_keys[pygame.K_RIGHT]:
							if MovePiece(1,0):
								Audio.PlaySound(assets["piece_move"])
				else:
					Gameplay.piece_horizontal_repeat_active = False
			
				#Move piece down repeatedly
				if pressed_keys[pygame.K_DOWN] and e.GameTimerEvent == "move_down_repeat":
					if MovePiece(0,1):
						Gameplay.piece_fall_active = False
						Audio.PlaySound(assets["piece_move"])
						#Increase score by a certain amount each cell down
						Score.current_score += Score.down_points
		
				#Move piece down automatically a number of cells over the course of a second
				if Gameplay.piece_fall_active and e.GameTimerEvent == "piece_fall":
					MovePiece(0,1)
				
		"""Gameplay logic"""
		#Checks if the piece is making contact with something below it and begin locking it into the grid or triggering game over
		if MovePiece(0,1):
			#No contact so reset piece to where it should be
			MovePiece(0,-1)
			#Pause the piece locking timer for a frame
			GameTimer.PauseTimer("piece_lock")
		else:
			#Contact - check if the player piece is above cutoff to trigger a game over
			if all(y < Gameplay.gameover_threshold for x,y in Gameplay.player_tetromino.block_positions):
				GameOver()
			
			#Contact - decrease newly-created timer for locking the piece
			if GameTimer.SetTimer("piece_lock",Gameplay.piece_lock_speed,-1):
				#Time's up - Lock the piece and remove timer
				GameTimer.RemoveTimer("piece_lock")
				LockPiece()
		
		#Clear events so they dont bleed over
		events.clear()

	"""Draw graphics"""

	#Game window background
	DrawWindow()
	#Tetris game board
	DrawBoard()
	#Player HUD
	DrawHud()
	#Settings menu
	if Settings.menu_active:DrawSettings()
	#Countdown timer
	if Gameplay.countdown_active:DrawCountdown()
	#Game over screen
	if Gameplay.gameover_active and Gameplay.gameover_screen_active:DrawGameOver()
	#Pause screen
	if Gameplay.game_paused and Gameplay.pause_screen_active:DrawPause()
	#Optional FPS
	if Graphics.render_fps:DrawFPS()
	#Render Screen
	pygame.display.update()

"""End of program - Thanks for playing"""
