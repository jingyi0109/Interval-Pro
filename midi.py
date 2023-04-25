# Write your code here :-)
from microbit import *

pin1.set_pull(pin1.PULL_UP)
pin2.set_pull(pin2.PULL_UP)
pin8.set_pull(pin8.PULL_UP)
pin12.set_pull(pin12.PULL_UP)
pin13.set_pull(pin13.PULL_UP)
pin14.set_pull(pin14.PULL_UP)
pin15.set_pull(pin15.PULL_UP)
pin16.set_pull(pin16.PULL_UP)

def midiNoteOn(chan, n, vel):
    MIDI_NOTE_ON = 0x90
    if chan > 15:
        return
    if n > 127:
        return
    if vel > 127:
        return
    msg = bytes([MIDI_NOTE_ON | chan, n, vel])
    uart.write(msg)

def midiNoteOff(chan, n, vel):
    MIDI_NOTE_OFF = 0x80
    if chan > 15:
        return
    if n > 127:
        return
    if vel > 127:
        return
    msg = bytes([MIDI_NOTE_OFF | chan, n, vel])
    uart.write(msg)

def show_note(note):            # Display LED function
    Notes = ['C' , 'c' , 'D' , 'd' , 'E' , 'F' , 'f' , 'G' , 'g' , 'A' , 'a' , 'B']
    led = Notes[note % 12]
    display.show(led)

def major_shift(note, shift):
    index = note % 12
    change = 0

    if (shift == 3):
        if (index == 5):
            change = 6
        else:
            change = 5

    elif (shift == -3):
        if (index == 5):
            change = -6
        else:
            change = -5
    elif (shift == 2):
        if (index == 0) or (index == 5) or (index == 7):
            change = 4
        else:
            change = 3
    elif (shift == -2):
        if (index == 4) or (index == 9) or (index == 11):
            change = -4
        else:
            change = -3
    elif (shift == 1):
        if (index == 4) or (index == 11):
            change = 1
        else:
            change = 2
    elif (shift == -1):
        if (index == 0) or (index == 5):
            change = -1
        else:
            change = -2
    return note+change

def minor_shift(note, shift):

    index = note % 12
    change = 0

    if (shift == 3):
        if (index == 8):
            change = 6
        else:
            change = 5

    elif (shift == -3):
        if (index == 2):
            change = -6
        else:
            change = -5
    elif (shift == 2):
        if (index == 3) or (index == 8) or (index == 10):
            change = 4
        else:
            change = 3
    elif (shift == -2):
        if (index == 0) or (index == 2) or (index == 7):
            change = -4
        else:
            change = -3
    elif (shift == 1):
        if (index == 2) or (index == 7):
            change = 1
        else:
            change = 2
    elif (shift == -1):
        if (index == 3) or (index == 8):
            change = -1
        else:
            change = -2
    return note+change

uart.init(baudrate=31250, bits=8, parity=None, stop=1, tx=pin0)
lastA = False
lastB = False

lastbtn1 = 1
lastbtn2 = True
lastbtn3 = True
lastbtn4 = True
lastbtn5 = True
lastbtn6 = True
lastbtn7 = True
lastswitch = True


note_now = 60
note_btn1 = 60
note_btn2 = 60
note_btn3 = 60
note_btn4 = 60
note_btn5 = 60
note_btn6 = 60
note_btn7 = 60

BUTTON_A_NOTE = 35
BUTTON_B_NOTE = 39

shift = 0

while True:
    a = button_a.is_pressed()
    b = button_b.is_pressed()
    btn1 = pin1.read_digital()
    btn2 = pin8.read_digital()
    btn3 = pin12.read_digital()
    btn4 = pin2.read_digital()
    btn5 = pin14.read_digital()
    btn6 = pin15.read_digital()
    btn7 = pin16.read_digital()
    switch = pin13.read_digital()

    if (btn1 == 0) and (lastbtn1 == 1):
        if (switch == 0):
            new_note = major_shift(note_now, -3)
        else:
            new_note = minor_shift(note_now, -3)
        note_now = new_note                 # The position of the note now
        note_btn1 = new_note + shift
        midiNoteOn(0, note_btn1, 127)
    elif (btn1 == 1) and (lastbtn1 == 0):
        midiNoteOff(0, note_btn1, 127)

    if (btn2 == 0) and (lastbtn2 == 1):
        if (switch == 0):
            new_note = major_shift(note_now, -2)
        else:
            new_note = minor_shift(note_now, -2)
        note_now = new_note
        note_btn2 = new_note + shift
        midiNoteOn(0, note_btn2, 127)
    elif (btn2 == 1) and (lastbtn2 == 0):
        midiNoteOff(0, note_btn2, 127)

    if (btn3 == 0) and (lastbtn3 == 1):
        if (switch == 0):
            new_note = major_shift(note_now, -1)
        else:
            new_note = minor_shift(note_now, -1)
        note_now = new_note
        note_btn3 = new_note + shift
        midiNoteOn(0, note_btn3, 127)

    elif (btn3 == 1) and (lastbtn3 == 0):
        midiNoteOff(0, note_btn3, 127)

    if (btn4 == 0) and (lastbtn4 == 1):
        note_btn4 = note_now + shift
        midiNoteOn(0, note_btn4, 127)
    elif (btn4 == 1) and (lastbtn4 == 0):
        midiNoteOff(0, note_btn4, 127)

    if (btn5 == 0) and (lastbtn5 == 1):
        if (switch == 0):
            new_note = major_shift(note_now, 1)
        else:
            new_note = minor_shift(note_now, 1)
        note_now = new_note
        note_btn5 = new_note + shift
        midiNoteOn(0, note_btn5, 127)
    elif (btn5 == 1) and (lastbtn5 == 0):
        midiNoteOff(0, note_btn5, 127)

    if (btn6 == 0) and (lastbtn6 == 1):
        if (switch == 0):
            new_note = major_shift(note_now, 2)
        else:
            new_note = minor_shift(note_now, 2)
        note_now = new_note
        note_btn6 = new_note + shift
        midiNoteOn(0, note_btn6, 127)
    elif (btn6 == 1) and (lastbtn6 == 0):
        midiNoteOff(0, note_btn6, 127)

    if (btn7 == 0) and (lastbtn7 == 1):
        if (switch == 0):
            new_note = major_shift(note_now, 3)
        else:
            new_note = minor_shift(note_now, 3)
        note_now = new_note
        note_btn7 = new_note + shift
        midiNoteOn(0, note_btn7, 127)
    elif (btn7 == 1) and (lastbtn7 == 0):
        midiNoteOff(0, note_btn7, 127)

    if a is True and lastA is False:
        shift = shift - 1

    if b is True and lastB is False:
        shift = shift + 1

    if (switch != lastswitch):
        note_now = 60
        shift = 0

    lastA = a
    lastB = b
    lastbtn1 = btn1
    lastbtn2 = btn2
    lastbtn3 = btn3
    lastbtn4 = btn4
    lastbtn5 = btn5
    lastbtn6 = btn6
    lastbtn7 = btn7  # 记住上一次按的是哪个扭
    lastswitch = switch

    show_note(note_now + shift)

    sleep(100)

