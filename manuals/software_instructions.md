# Typhoon Roaster Software Instructions

> **Source:** Software_Instructions.pdf  
> **Content:** Full extracted text from original document

---

Interface
Interface
1. The main window of the application includes the following key elements:
2. Control Panel – Allows you to start the Cyclone, preheat the roaster, begin and stop
roasting, add events during the roasting process, and save roasting results as history or a
profile.
The visibility of control elements changes during operation. A detailed description of the
icons is provided below.
3. Menu Panel – Enables navigation between different application windows:
4.
Current roast
Roasting profiles
Journal of Roasting
Settings
Notifications
5. Telemetry block- displays the current state of the roster
6. Crack block- displays crack information during roasting
7. Schedule- displays historical data of roaster parameters during roasting, roasting progress
bar
8. Roasting stage- shows what state the roaster is in, whether the warm-up, roasting and/or
cooling stage is active, whether the roaster is ready for roasting.
Control Panel

The visibility of the buttons on the control panel may change while you are working with the
program.
Start menu
Preparing- start heating up
Manual roasting- manual roasting start
Repeat- repeat the last roast
Heating process
Stop- stop heating
Roasting process
Stop- stop roasting
Charge- loading coffee into the roasting chamber
Turning point- event setup Turning point manually
First crack - event setup First crack manually
Stop First crack - event setupStop First crackmanually
Second crack - event setupSecond crackmanually
Stop Second crack - event setupStop Second crackmanually
Drop- end of roasting, unloading coffee from the roasting chamber, setting an
eventDropmanually
Complete- saves the current roast to the roast history
To profile- saves the current roast to the roast history and converts it to a profile
Program settings
The settings control panel contains the following items:
Roasting settings- allows you to customize units of measurement, display style,
application language and other roasting parameters.
Chart settings- allows you to customize axis boundaries, line types, thickness and
color
Other Settings - additional settings block
To save changes, you must click the button Save.

To reset to factory settings, you need to press the button Set to default, then press Save.
Roasting settings
Roasting settings
● Weight- units of weight measurement
● Temperature- units of temperature measurement
● Language- program interface language
● Theme- color scheme of the application
● Rate of Rise (RoR)- RoR calculation time
● Cooling time- time for cooling the beans after unloading from the roasting chamber
● Repeat from event- the event that starts the repetition of the roast profile/history
● Temperature coefficient- temperature correction coefficient
Chart settings

Chart settings - Plot axes
Graph settings - Data graphs
Chart settings - Event lines

Settings schedule - Roast phases
The chart settings are divided into 4 tabs with settings:
● Plot axes- settings for displaying graph axes
o X-axis max (Time)- maximum time on the X axis
o X-axis step (Time)- grid step along the X axis
o Y-axis left max (Temperature)- maximum temperature of the left Y axis
o Y-axis left step (Temperature)- grid step along the left Y axis
o Y-axis right max (RoR)- maximum RoR value along the right Y axis
o Y-axis right step (RoR)- grid step along the right Y axis
● Data graphs- settings for displaying data on the graph
o Reference line type- type of reference roast chart line
▪ Solid (Solid)
▪ Dashed (Dash)
▪ Point (Dot)
o Graph line type- type of current roast graph line
▪ Solid (Solid)
▪ Dashed (Dash)
▪ Point (Dot)
o Current roast graph opacity- transparency of the current roasting graph
o Reference roast graph opacity - transparency of the reference roasting chart
o Colors of graph lines
● Event lines- settings for displaying events on the chart
o Event line style- event line type
▪ Solid (Solid)
▪ Dashed (Dash)
▪ Point (Dot)
o Event line width- event line thickness
o Event Line Color
● Roast phases- customization of display of roasting progress bar and roasting phases
o Drying end (Temperature)- temperature of the end of the first phase of roasting
o Phase 2 end (Event)- event of the end of the second phase of roasting (not
editable)
▪ First crack event
o Development end (Event)- third roasting phase end event (not editable)
▪ Drop event
o Phase colors on the roasting progress bar

Other settings
Other settings - PID controller
Other settings - Frequency driver

Other settings - Remote control
Other settings - Actuators
Other settings are divided into 3 tabs with settings:
● PID controller- PID controller settings:
o Empty roaster- for an empty roaster. The settings are used during warm-up
o Loaded roaster- for a roaster with coffee in the roasting chamber. The settings
are used during roasting
● Frequency driver - frequency settingsof the converter:
o Baud rate
o Parity
o Stop bit
● Remote control- remote access settings to the roster
o ID - RustDesk client ID
o Access password- input field permanent access password
o Random password- generates a permanent access password
● Actuators- actuator operation settings
o Default exhaust gate position- default position of the exhaust actuator
o Coffee loading delay- the time during which the coffee loading damper will be in
the open position
● Update app- update the application. The update process is described in the section
"Updating the application"
Roasting profiles
The profiles page displays all saved roast profiles. To interact with a profile, select its card and
choose the required action from the pop-up menu:
Play- repeat profile
Edit- edit profile data

View- view profile data
Delete- delete profile
History of Roasting
The Roast History page displays all saved roast histories, grouped by date. To interact with a
history entry, select its card and choose the desired action from the pop-up menu:
Repeat- repeat frying
View- view roasting data
Delete- remove the roast
To profile- convert roast to profile
Service mode

The service mode is intended for servicing the roaster.
To move to the service mode, you need to click on the logoTyphoon roasterin the upper left
corner of the screen.
The service mode window displays the following information:
▪ Calibration- actuator and ejector calibration statuses.
The field displays the value in the control board memory.
Green color means calibration is finished, red - calibration was not performed. Coloring
the field in green does not mean that there are no equipment errors, they are displayed
inStates
▪ States- equipment statuses:
▪ Initialization- board initialization flag
▪ Last button- the last pressed button (Start / Stop)
▪ VFD- frequency drive status
▪ Undefined - not defined, no connection to control board
▪ Connected - the frequency drive is connected and working properly
▪ Disconnected - the frequency drive is not connected
▪ In error - frequency drive is in error state
▪ Loading gate- status of the loading actuator
▪ Undefined - no connection to control board
▪ Not initialized - initialization error
▪ Stacked - jammed
▪ Ok - calibrated, no errors
▪ Unloading gate- unload actuator status

▪ Undefined - no connection to control board
▪ Not initialized - initialization error
▪ Stacked - jammed
▪ Ok - calibrated, no errors
▪ Exhaust gate- state of the exhaust actuator
▪ Undefined - no connection to control board
▪ Not initialized - initialization error
▪ Stacked - jammed
▪ Ok - calibrated, no errors
▪ Thermocouples - status thermocouple
▪ Undefined - no connection to control board
▪ 0x01 - Thermocouple Open-Circuit Fault
▪ 0x02 - Overvoltage or Undervoltage Input Fault
▪ 0x04 - Thermocouple Temperature Low Fault
▪ 0x08 - Thermocouple Temperature High Fault
▪ 0x10 - Cold-Junction Low Fault
▪ 0x20 - Cold-Junction High Fault
▪ 0x40 - Thermocouple Out-of-Range
▪ 0x80 - Cold Junction Out-of-Range
▪ Temperature- current temperature value from sensors
▪ Beans- bean temperature
▪ Exhaust- temperature in the hood
▪ Power- current and target power value
Clicking on the right value (target value) opens a pop-up window where you can change
this value.
▪ Heater- heater
▪ Fan- exhaust fan
▪ Equipment- current and target state of equipment
Clicking on the right value (target value) opens a pop-up window where you can change
this value.
▪ Loading gate- loading hatch actuator
▪ Unloading gate- unloading hatch actuator

▪ Exhaust gate- actuator of the hood hatch
▪ Ejector- ejector
▪ Cooler mixer- condition of the cooler mixer
▪ Cooler exhaust- condition of the cooler exhaust
▪ PID- PID controller coefficient tuning block
▪ Kp, To, Kd- PID controller coefficients
▪ Enabled/Disabled- PID controller activity switch
▪ Target temperature- target temperature value (the bean temperature value is
used).
Clicking on a value opens a pop-up window where you can change that value.
▪ Graph - displays the temperature value
▪ Clear data- clears the schedule
▪ Export data- allows you to save graph data to a file{current_date_time}.csv
IMPORTANT: when switching to service mode during roasting, changing parameters and
enabling the PID controller is disabled.
IMPORTANT: when switching to service mode during warming up, temperature maintenance
stops, the roaster goes into standby mode. When exiting service mode, if warming up was started
earlier, it continues as inter-batch.
IMPORTANT: the graph displays data received within 30 minutes from the start of the program
or pressing the buttonClear data.
IMPORTANT: when exporting, data received within 30 minutes from the start of the program
or pressing the button is saved.Clear data.
Temperature correction factor
The program uses a temperature correction factor. It is applied to all temperatures measured by
the program by adding it to the current temperature value.
You can adjust the coefficient in the settings:Settings → Roast settings → Temperature
coefficient
IMPORTANT: the coefficient value is configured for each roaster, not stored in profiles and
roast histories.
Automatic Event Detection Algorithms
Reaching temperature during warm-up and inter-batch
preparation
During warm-up and inter-batch preparation, the current temperature in the roasting chamber and
the target temperature are analyzed. As soon as the current temperature reaches the target

temperature with an interval of 0.4%, the program considers that the target temperature has been
reached.
Loading coffee - Charge event
When you press the coffee loading button Charge the program starts analyzing the current
temperature in the roasting chamber. If the temperature drops by more than 2 degrees within 2
seconds, the program identifies this as an eventCharge.
Turning point event
After the eventChargethe program continues to analyze the current temperature in the roasting
chamber. After loading cold coffee into a hot roasting chamber, the temperature inside the
chamber decreases until it equals the temperature of the beans - until the beans warm up, then it
begins to rise. The lowest point of the temperature change - the temperature change trend is zero
or positive, is identified as an eventTurning point.
Coffee unloading - Drop event
When you press the coffee discharge button Drop the program starts analyzing the current
temperature in the roasting chamber. If the temperature drops by more than 2 degrees within 2
seconds, the program identifies this as an eventDrop.
Conditions for finishing roasting
During roasting in automatic mode, the program analyzes roasting indicators that affect the
completion of roasting. The following conditions for the completion of roasting are
distinguished:
● The grain temperature has reached the reference level
● The temperature increase exceeds the reference value by more than 15%
● DTR more than 10%
● DTR exceeds reference by more than 25%
● Total roasting time exceeds reference by more than 25%
Initialization and self-diagnosis
Each time the roaster is started, the control board performs self-diagnostics. Depending on the
supportedfunctionalityThe following situations are possible:
▪ Self-diagnosis process in progress - displayed until self-diagnosis is completed or an error
occurs.
▪ There is no connection with the frequency drive
▪ Frequency drive operation error
▪ Error in thermocouple detection

▪ Actuator initialization error
▪ Actuator stuck
▪ Error while moving the ejector
Actuator control
Actuator position designations
● 0 - actuator in closed state,
● 9 - actuator in open position.
Pre-start warm-up
When starting warm-up:
● Load actuator position -closed,
● exhaust actuator position - the position specified inprogram settings (Settings →
Other settings → Actuators → Default exhaust gate position).
During the warm-up process, the user can independently change the positions of the actuators.
Hand roasted
When you press the coffee loading button ChargeThe coffee loading actuator is switched
toopenposition and, after the time specified inprogram settings (Settings → Other settings
→ Actuators → Coffee loading delay), returns to the closed position.
During the roasting process, the user can independently change the positions of the actuators.
Automatic roasting
IMPORTANT: Changing any roaster parameter switches roasting to manual mode.
When starting automatic roasting - the user selected the type of roasting profile repetition or
selected a roasting repetition from history:
● Load actuator position -closed,
● exhaust actuator position - position at the time of the eventChargereference profile, if
absent - the position specified inprogram settings.
When the user presses the coffee loading button - Charge,
● position of the loading actuator - is translated intoopenposition and, after the time
specified inprogram settings, returns to the closed position
● position of the exhaust actuator - depending on the type of repetition and the "Repeat
from event" parameter in the program settings:
o by temperature - the position does not change,

o by parameters - repeats the position in the reference profile,
o by events - changes depending on events.
Preparation between batches
The algorithm works when the user presses the coffee loading button - Drop,
● Load actuator position -closed,
● position of the exhaust actuator - as in the previous roastat the time of the Charge
event, if absent - the position specified inprogram settings.
During the preparation process, the user can independently change the positions of the actuators.
Ejector control (for 10 kg model)
Note: The operator has no way to directly influence the position of the ejector.
Note: Ejector control is possible for roaster models that implement this functionality.
Hand roasted
When you press the roasting start button Manual roastingthe ejector is translated
intostartingposition.
When you click the unload button DropThe ejector is translated intoextremeposition and
then returns tostartingposition.
Automatic roasting
When automatic roasting starts, the ejector moves tostartingposition.
When you click the unload button DropThe ejector is translated intoextremeposition and
then returns tostartingposition.
When any of theConditions for stopping roasting
● for roasters without ejector
o a message (pop-up) about the condition that has been triggered is displayed on the
screen
o The operator decides independently whether to complete or continue roasting;
coffee is unloaded manually.
● for roasters with ejector
o the ejector is moved to the extreme position and then returns to the starting
position
o A pop-up notification appears on the screen to notify you that roasting is
complete.
Preparing for roasting

Note:The operator can interrupt the preparation process without waiting for its completion and
start the coffee roasting process.
Primary preparation (warm-up)
Primary preparation consists of warming up the roaster skin.
Primary preparation algorithm:
1. Press the START button on the roaster.
2. Go to windowCurrent roast.
3. Press the button Preparing.
4. In the pop-up window, specify:
1. target temperature
2. warm-up time
5. PressApply.
6. In panels Roasting stages active die Prepare, information about the warm-up progress
will be displayed on top of the graph:
1. Heating- heating to the temperature specified in step 4
2. Temperature holding- maintaining the temperature for the time specified in step
4
7. Wait until the roaster warms up - reaches the set temperature and is maintained for the set
time.
8. Once the preheating is complete, a pop-up window will appear informing you that the
roaster is ready for roasting.
9. In panels Roasting stages active die Ready. The temperature maintenance algorithm
continues to operate.
10. PressOk.
The heating process can be stopped by pressing the buttonStop. This action will not stop the
temperature maintenance algorithm, but will allow you to perform other actions with the
program. The temperature maintenance algorithm also continues to work after the timer expires.
Inter-batchive preparation
Inter-batch preparation starts automatically after each roast.
Inter-batch preparation involves warming up the roster to event temperature.Chargeprevious
roasting or a repeated profile.
Warming up is similar to primary preparation with the only difference being that the
stageReadylights up immediately after reaching the desired temperature.
Hand roasted coffee
It is assumed that the roaster is preheated and ready to roast.
1. Go to windowCurrent roast.
2. Press the button Manual roasting.
3. In the window that opens, enter the required information and clickStart.

4. Press the button Charge. The fan power will drop to20-40%
5. Load coffee. The program will automatically detect the eventCharge. The graphs will
start to be drawn. In the panelRoasting stages active die Roasting.
6. The program will automatically detect the event.Turning point. If this does not happen,
press the button Turning point.
7. Press the button First crack. The calculation of values in the panel will
begin.Crack block.
8. (not necessarily) Press the button Stop First crack.
9. (not necessarily) Press the button Second crack.
10. (not necessarily) Press the button Stop Second crack.
11. Press the button Drop.
The power of the heating elements and the fan will drop to 0% for 5 seconds.
The calculation of values in the panel will stopCrack block
Drawing of charts will stop
The inter-batch preparation protocol will start in the panelRoasting stagesactive
plaquePreparing and a cloak Cooling, if cooling time is set
12. Press the button Completeto save the roasting in history or To profile- to save
as a profile.
Automatic coffee roasting (profile repeat)
IMPORTANT: This assumes the roaster is preheated and ready to roast.
IMPORTANT: Profile repeat starts with the event specified in the roast settings -Charge or
Turning point.
IMPORTANT: Changing any roaster parameter switches roasting to manual mode.
IMPORTANT: ONLY events are automatically detectedCharge, Turning point, Drop. All
other events are set MANUALLY.
IMPORTANT: When playing a roast from a roast history, it is similar to repeatingby roster
parameters.
Repeat roasting according to roaster parameters
With such repetition, the program automatically sets the values of the roaster parameters (the
power of the heating elements and the fan), with a high degree of probability it will be possible
to obtain the most similar temperature graphs.
Option 1 - from the windowCurrent roast
1. Go to windowCurrent roast.

2. Press the button Repeat. The fan power will drop to 20%.
3. Press the button Charge. The fan power will drop to20-40%.
4. Load coffee. The program will automatically detect the eventCharge. The graphs will
start to be drawn. In the panelRoasting stages active die Roasting.
5. The program will automatically detect the event.Turning point. If this does not happen,
press the button Turning point.
6. Press the button First crack. The calculation of values in the Block Crack panel
will begin.
7. (optional)Press the button Stop First crack.
8. (optional)Press the button Second crack.
9. (optional)Press the button Stop Second crack.
10. Press the button Drop.
The power of the heating elements and the fan will drop to 0% for 5 seconds.
The calculation of values in the panel will stopCrack block
Drawing of charts will stop
The inter-batch preparation protocol will start in the panelRoasting stagesactive
plaquePreparing and a cloak Cooling, if cooling time is set
11. Press the button Completeto save the roasting in history or To profile- to save
as a profile.
Option 2 - from the Roasting History window
1. Go to windowHistory of Roasting
2. Select the roast card you want to replicate. This roast is considered the reference.
3. The button is pressed in the card pop-up menu Repeat
4. The program will automatically switch to the window.Current roast. The chart will
show reference roast lines. The fan power will drop to20-40%
5. Press the button Charge
The fan power will drop to20-40%
6. Load coffee. The program will automatically detect the eventCharge
The graphs will start to be drawn
In panels Roasting stages active die Roasting
7. The program will automatically detect the event.Turning point. If this does not happen,
press the button Turning point

8. Press the button First crack.
The calculation of values in the panel will begin.Crack block
9. (optional)Press the button Stop First crack
10. (optional)Press the button Second crack
11. (optional)Press the button Stop Second crack
12. Press the button Drop.
The power of the heating elements and the fan will drop to 0% for 5 seconds.
The calculation of values in the panel will stopCrack block
Drawing of charts will stop
The inter-batch preparation protocol will start in the panelRoasting stagesactive
plaquePreparing and a cloak Cooling, if cooling time is set
13. Press the button Completeto save the roasting in history or To profile- to save
as a profile.
Option 3 - from the Roast Profiles window
1. Go to windowObžarok profiles.
2. Select the roast card you want to replicate. This roast is considered the reference.
3. The button is pressed in the card pop-up menu Play.
4. In the pop-up window, select the profile repetition type.By parameters.
5. The program will automatically switch to the window.Current roast. The chart will
show reference roast lines. The fan power will drop to20-40%.
6. Press the button Charge. The fan power will drop to20-40%.
7. Download. The program will automatically detect the event.Charge. The graphs will
start to be drawn in the panel.Roasting stages active die Roasting.
8. The program will automatically detect the event.Turning point. If this does not happen,
press the button Turning point.
9. Press the button First crack. The calculation of values in the panel will
begin.Crack block.
10. (optional)Press the button Stop First crack
11. (optional)Press the button Second crack
12. (optional)Press the button Stop Second crack

13. Press the button Drop.
The power of the heating elements and the fan will drop to 0% for 5 seconds.
The calculation of values in the panel will stopCrack block
Drawing of charts will stop
The inter-batch preparation protocol will start in the panelRoasting stagesactive
plaquePreparing and a cloak Cooling, if cooling time is set
14. Press the button Completeto save the roasting in history or To profile- to save
as a profile.
Repeat roasting by temperature
With this repetition, the program automatically sets the roaster parameter values by analyzing the
temperatures of the current and reference roasts.
1. Go to windowObžarok profiles
2. Select the roast card you want to replicate. This roast is considered the reference.
3. The button is pressed in the card pop-up menu Play
4. In the pop-up window, select the profile repetition type.By temperature
5. The program will automatically switch to the Current Roast window. The chart will
display the reference roast lines. The fan power will drop to 20-40%
6. Press the button Charge
The fan power will drop to20-40%
7. Load coffee. The program will automatically detect the eventCharge
The graphs will start to be drawn
In panels Roasting stages active die Roasting
8. The program will automatically detect the event.Turning point. If this does not happen,
press the button Turning point
9. Press the button First crack.
The calculation of values in the panel will begin.Crack block
10. (optional)Press the button Stop First crack
11. (optional)Press the button Second crack
12. (optional)Press the button Stop Second crack
13. Press the button Drop.
The power of the heating elements and the fan will drop to 0% for 5 seconds.
The calculation of values in the panel will stopCrack block
Drawing of charts will stop

The inter-batch preparation protocol will start in the panelRoasting stagesactive
plaquePreparing and a cloak Cooling, if cooling time is set
14. Press the button Completeto save the roasting in history or To profile- to save
as a profile.
Repeat roasting by events
It is assumed that the roaster is preheated and ready to roast.
With this repetition, the program automatically sets the roster parameter values when events
occur.
1. Go to windowObžarok profiles
2. Select the roast card you want to replicate. This roast is considered the reference.
3. The button is pressed in the card pop-up menu Play
4. In the pop-up window, select the profile repetition type.By events
5. The program will automatically switch to the window.Current roast. The chart will
show reference roast lines. The fan power will drop to20-40%
6. Press the button Charge
The fan power will drop to20-40%
7. Load coffee. The program will automatically detect the eventCharge
Roaster settings will change to the same as the reference roast during the event.Charge
The graphs will start to be drawn
In panels Roasting stages active die Roasting
8. The program will automatically detect the event.Turning point. If this does not happen,
press the button Turning point
9. Roaster settings will change to the same as the reference roast during the eventTurning
point
10. Press the button First crack.
Roaster settings will change to the same as the reference roast during the eventFirst
crack
The calculation of values in the panel will begin.Crack block
11. (optional)Press the button Stop First crack
Roaster settings will change to the same as the reference roast during the eventStop First
crack
12. (optional)Press the button Second crack
Roaster settings will change to the same as the reference roast during the eventSecond
crack

13. (optional)Press the button Stop Second crack
Roaster settings will change to the same as the reference roast during the eventStop
Second crack
14. Press the button Drop.
The power of the heating elements and the fan will drop to 0% for 5 seconds.
The calculation of values in the panel will stopCrack block
Drawing of charts will stop
The inter-batch preparation protocol will start in the panelRoasting stagesactive
plaquePreparing and a cloak Cooling, if cooling time is set
15. Press the button Completeto save the roasting in history or To profile- to save
as a profile.
Profile Events
To view and edit profile events, you must:
1. go to the profiles page,
2. select the desired profile and press the button View,
3. in the window that opens, go to the tabEvents.
The page will display a list of events and roster parameters at the time of the event. This data is
used when repeating the profile by events.
Roasting Events
Roasting events - events that occur during roasting, detected by the program or the operator.
These include Charge, TP, FC/SC, Stop FC/SC, Drop.
Custom Events
Custom Events - Events set by the operator based on roast time or bean temperature.
Adding a custom event
To add an event, you need to click on one of the buttons between the event cards, depending on
the type of event being added:
1. Time- time event, triggered after a specified time has passed since the previous event
2. °C/°F- temperature event, triggered when the set temperature is reached

In the opened window for the eventTimeyou must specify the time after which the roster
parameters will change; for a temperature event - the temperature upon reaching which the roster
parameters will change. Next, to add an event, you must click the buttonAdd, to cancel changes
-Cancel.

Time event
Temperature event
Deleting a custom event
To delete a custom event, you need to click on the button Removeon the event card.
To save changes, you need to click on the icon Savein the upper right part of the screen.
Changing Roster Parameters
To change a roster parameter, click on it (the round indicator), set the desired value in the
window that opens, and click on the check mark. To cancel the change in value, click on the
cross or outside the pop-up window.

To save changes, you need to click on the icon Savein the upper right part of the screen.
Editing a comment
To change the comment parameter for an event, you need to click on the button Edit, in the
window that opens, make changes and click on the buttonSave. To cancel the change of value -
click onCancel.
To save changes, you need to click on the icon Savein the upper right part of the screen.
Program update
In the program interface
IMPORTANT: This update method should always be used!
1. Download the deb package for the required architecture to a flash drive (for example,
TyphoonRoaster_***_arm64.deb).
IMPORTANT: there is no need to rename the downloaded file, since the update search
occurs, including by file name, by template.
2. Insert the flash drive into the Raspberry PI
3. In the application go toSettings → Other settings, press the buttonUpdate app.
4. Review the information in the pop-up window and click the buttonApply
5. Wait until the update is complete
If a suitable update file is not found, the application will display a pop-up window
describing the problem. Possible problems:
1. Update file not found.
2. Update file found, but software version is lower than or equal to current
6. After a successful update, the application will display a pop-up window warning you to
restart it. You must click the buttonApplyand wait for the application to restart
Via command line
IMPORTANT: This update method should NOT be used during normal operation of the roster!
With a repository
1. Connect Keyboard to Raspberry Pi
2. Press on the keyboardCtrl + Alt + F2
3. Enter login and password. Password input is not displayed for security reasons.
4. Execute command
sudo apt-get update && sudo apt-get install --only-upgrade typhoonroaster
5. After the update is complete, restart the OS with the command
sudo reboot

From a local file
1. Connect Keyboard to Raspberry Pi
2. Connect a flash drive with the program to Raspberry Pi
3. Press on the keyboardCtrl + Alt + F2
4. Enter login and password. Password input is not displayed for security reasons.
5. Execute command
sudo dpkg -i /media/user/sda-usb-VendorCo_Product/TyphoonRoaster*.deb
6. After the update is complete, restart the OS with the command
sudo reboot
Remote Roaster Management
Connecting to a Roster
IMPORTANT: To connect remotely to the roster, you must have a stable Internet connection.
First, you need to make sure that in the roster settingsSettings → Other settings → Remote
controlin the fieldIDcontains the client number for connection - a string of numbers,
fieldPasswordnot empty. In case of absenceIDyou need to check your Internet connection. If
there is no password, you need to enter it manually or generate it by clicking on the
buttonRandom passwordand save - click on the buttonSave.
To enable remote control, you need to install the RustDesk application on your computer
(https://rustdesk.com/). In the fieldControl Remote DesktopenterIDroster and press the
buttonConnect.
After a successful connection, a window will appear asking you to enter a password. You must
enter the same password as indicated on the roster and click the buttonOk.
If an error occurs during the connection process, you should check that the password is entered
correctly, that the Internet connection is available, the Internet connection parameters, or refer to
the RustDesk documentation (https://rustdesk.com/docs/en/).

Other features
RustDesk's capabilities are described in the program's documentation
(https://rustdesk.com/docs/en/)
Known issues
▪ It should take about 2 minutes from the time the roster is launched before it can be
connected to remotely.