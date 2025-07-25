# Grind-Guard
A neat app that forces you to not be lazy 

Hello, thanks for downloading my repo. I made this as a challenge / due to boredom and gave myself a 1 hour time limit to complete this, it should work just fine. 

The point of this is to reduce being lazy.. Reminds you, hey do this or you cant use your computer fucker, odv I could've added more "assurance" features like not being able to click "I'm Done" for about 10 minutes or so, ect, however it's not that deep. I did add a no escape function meaning your not opening your task manager (this is optional in the GUI) but the main point of this is so you do something good for yourself. 

You're free to fork this idc, I also did just wanna upload something cause why not.

------------------------------------------------------------------------------------------------------------

I ran out of time at the end, so the transparency of the overlay is fucked but if you want to change it:

Remove or comment out both the self.attributes("-alpha", …) line and the self.after(0, self._fade_in) call. (In overlay.py if your not smart and have no idea which file to fuck with)

Or: Option B: Force full opacity immediately by just replacing those two lines with self.attributes("-alpha", 1.0)

ORRRRRR: Tweak the 0.8 in _fade_in to your desired final opacity (e.g. 1.0 for fully opaque). Easy as shit.

--------------------------------------------------------------------------------------------------------------------
