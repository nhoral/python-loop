DESCRIPTION

This is a python script executes macros based on the presence or absence of images on the screen.  It uses the OpenCV
library (via pyautogui) to find a close match to the images you save.

INSTALLATION

On Windows and Mac, you can quickly create a Python environment by downloading Anaconda.  You can download here:
- https://www.anaconda.com/download
- Search for Anaconda Prompt on your Windows Search Bar

Anaconda includes a visual explorer GUI (not what we want) and an Anaconda Prompt.  The Prompt is a terminal that we can
execute commands in, basically identical to a Command Prompt.

When you have Anaconda Prompt open, you can navigate to where you have extracted this project.  Once in the folder, you can
just run "python loop.py".  This will begin the script.

Most likely, your python installation is missing some packages required by the project.  You can install missing packages by
running:

- pyautogui -> pip install pyautogui
- OpenCV -> pip install opencv-python
- keyboard -> pip install keyboard
- input -> pip install input

RUNNING

With those packages installed, you should be able to start the script.  You should see "Started" appear in the Anaconda Prompt
terminal.  By default, the important keys are:
- Keyboard Key "M" or XboxController Key "X" will engage the script to search the screen and execute your macros
- Keyboard Key "N" will stop the script

Either key can be changed in the loop.py by changing DEFAULT_KEYBOARD_KEYT and STOP_KEY respectively.

SAVING IMAGES

In the images folder, I included the images I use for example.  These will be useless to you, since my UI is running in 4K, but should show roughly how they look.  The name of the image (e.g. immolation.png) is very important, since this will be the name you will reference in your macros.

The easiest way to grab the icon is to use the "Snipping Tool" app that is included in Windows 10.  This will let you select a portion of the screen and save it as a PNG.  Be careful to only snip the static portion of the icon (e.g. no background or transparent icons).

WRITING MACROS

In the profiles folder, there is two example entries for Warlock and Rogue with a single macro.  The loop is currently pulling from the rogue macros, but you can change that by changing the line in loop.py that sets the macros to use:

- from profiles import rogue -> from profiles import myNewProfile
- macros = rogue.macros -> macros = myNewProfile.macros

A macro is a collection of predicates (conditions to evaluate) and the key to press when the macro is true.  The first macro to evaluate as true will press the key, and all subsequent macros will be ignored.  This might be something we need to change later depending on how cumbersome it is.

If no macros are matched, the script will press the DEFAULT_KEY defined in loop.py.

WEAKAURAS EXAMPLES

-> Combo Points:
!WA:2!Ln1tpUnru8eLk1TgjujqxjKGTlRGkbc1dO2vOIeAJZ60nlztc2UBwKIuYypJJhQZmUZmojBfxiId9cxYNauoZPCHJG2dCGtwr9tqp1dCA)cS8gBRWwWhSEZBE)73B(9RCJQJRIRIFXEIzDccKe1rh8t394FPuPsIZlC8hjd)TxdowHy(HCrxoLP8QB121Y2K6ZzHZvc6OreH8TVNOW8pnvNhtmtyu1RKjEKjeMYjjiGoB1G61CCh44wZ21oZVDx(uIyEIKmqh)W0B5fhHoNiweRVqxOBnxgtIIAILgxOJtgYNwNlvdTzOXePXME0vqGEy701QvR16i3uIHlXepycCbBXrwT624jTwKWkMxJ43b5ROtiU5NpHJj)APlbKsemu0Pa4OC2pVaXOJrkWCFBPcjuns3YKXzKliijXrjiSrQWBUgNiYIAGUZcjb2sy5CDm62NUJ5yeLb5MUt6DVz6UPFu6EP74fqzuz4)1TPImtfctVeP0LLeoxWvzLV8sa32KrGP8Z2oDR1WrpK)thj4jm8lUtCvDUW2cH5tpl)5Ss87N5m7xaxaWzGSWiDNfBUBVprgF7RLEDEexCC5YLR8QCVKOGmQq6nIF3mpOefxVC87rXQqZAWXlZ7cDgbN58hxNZH(U8zP8fz3)9jsfn480BSmdyexWPz7oTTs3saishZYSa9ZMHkW3IIXNPIVDdb957(TjimSCq766(gOUOtFqP1zoNYf4Ecu88EfgR3ui9lJzB4TSa2xJTdq8)V0yBwA)BnCOpN8Pfy8S3aJtOsQxezOxiHokeuzh8S)sRY8YHCOzehHpDHMY6hHKYHEkueqO32ECsKIAycca)TtBAyND998Ku2OiITDNh)elWTPeAT((SvEIGObNMfh)E1Bv7KUUDmBvR(3u7WdB628ulVXuHGlcxkYypzIIIexaJjdRt12SLv7dtDIFutToia5t6xdJ7WK97rqpTgWgL9pHGPO(U55k778SeKGmOrsuuVqQISkqakuqzaVnvwdueyZ0jwtELglvC)j5kRT(8)Epko(o15J947(dpiBT)OS)YV6Y8fAdDL0tQNtDBlR22OO4quf7PAM1rh81V1X)(vxDLhO1cOJm(IekEvdrh)979GOJN9ybLP7fj02FdtwO18WKSF6hAycIpLr6hBSulwP5t4kkl)rgozS4Au(Qs7hE)V8(pS6KxE2)8d

-> Energy:
!WA:2!1rvqVTrruyBmsjScHASO5qLQuJbcsvOQGlnQcL0gVoRXP1j2mEBcbfj7z39T7oK1ZSmZSoXio5tCHl(gNcksCJt5paLwXnqAKf)c6zqiLdCnmZ60ieQC7nZ899EFZ3BEtXgLhuoOCW3uHFC7WqbiBUX4PF9VvOqb(Ol34Pz9)1Fimm(mm1pMX7WiuPxDNDCDq2eFgnESKtIIaU4TwMFz4FBlhLc2zuI8fImpyiqLD4qi5yu3ooTAHszhb8BxP6kv(OvEr(IESuGJLm(Tl)GkRT(Kmb0l)G4NzcfXSJQZeY(JnRmjUpkpTOogqtYHAk6CJfPqsYwbcl1B4LMGhbCefpaewxjLUzHAPCwV61662RRBnK70RkNjh9pna80yC1X8MoT604jTMKrV8YzLUa2xsgcUZwVnla(XcNRTfGtXj7QDccJ(TtWuYaSuhUksiXCzd182ugfEgGfqxjhOrY45MgKXZr1ZuzUa0wAGySbJP8QLShGjunx1sQkZPEh17QEp1sEHekre)F32wchlJ1QxGLM0cXJ5mzE6lEQ(2JGiDO4glQMFQEPh2)WiolJg4fdKOyD3FJ9)UNF37w1lNgeBNWWb7M3m8tWcrFpjor7GlIgKLijw2AZ2Frvvlu(Xl7ji0OeaHA)jpXrVTTG8vG58ZnklJd7XXPgdl9TR3Q22DCBB3Qw9hxBZn3YDRDD8gq4Cgp(uEUqZ9)ljoXtx3advKDlND2uTw6hVLXYdX(Wb1ccAtfhShGpSM(IloyBiGGpWDgxXbD)Ymmh61iljzVyIeolKRFsOBcyjU0uCMu)YUDQXNewNkz(dN1eN)d(JkKaphkWJgD(SbGggMgL51ToYXzheojngxcDejqg3CJ1o5X)0fxCHNUngsISQMrcoRXE7tJ3VDnF5xWjutUHyKplHXFuXIflXnpN0vEv1TSS19vPL69To18oGKV)NVmYpg8pSHAUsJhI5eS2luVzfwA5hGgItYa9Ge3pgtJaXnwwHEuXMp8NxyHBvOWRvQ04uUz0sos1AzvhtouF6LKvi94NQ7mkLA(WV)AxtZPqjL7Re7QVeRg6FEZBUHgAX)pS3)FH9xU(11PT4RcBL1xxHQ(HRCfATY)Rto5PVufNrOHm(SXiRjcijm))h1RxwGU3DU)DUx5H)(N9p

-> Immolation
!WA:2!DnvZUnsrqyhfHaMdiHfkhwXHvzr5cjbPajKBSE8AlNfN4OEgwcNS7z6AMUj909OU7X2jNqwCajGlw8e4ZCYpbO8emYAFc2dCIt5jGQTJ5a9L(NQ6Q(((QQ2PBZIMSMSF5Zwis1QiDLjf(0gKuTuBE9U4YC3GSml469xX7VFdCTKQs5AZ1AHYL0UZvXDiRs1Ajtprfnruc8h2ETdlh4gAQtOv2Ziwh14csYekHLFWCMEyAL1Pl4VJlyWqQuomxQNy5HOhUGzoJiphm2p6aZth)BtLfUIwaJMtRmufEY(St(YV68fmiPkll(UsW0Rf5YUFxFdcGbk5DJiWyaHApGkDCY6)eSOcZqNPcRZYFNTkzTlxBGmXus01D63FMTeKYly2GqVRji0Zb3QcQlLd2iUEYa1d21BTq(ng(VOeH4qmD5W2TIIhgf3Ieh6qyr8a(Kee)eOGpVs9eLck)y66aeV5(LAg8NnEefxWOOY3G8hvVF)XBbOSfcQuhHI6jFovjk8NuNv)HDFaOwiYzavUJ)(1ViuPvWkgMsVhd9aWybScZSZ8U6fQ6ddlOcv36ph)q9H1hvFC9xG7b))xqX1sD(yb8finjqUVG(S9QFXk8Acn92CJUsXs4GiN769YVEf95nAStOutzVzoY5HPsQ1ocLrjkr7rkQKorqONp7vFEazT5dsScvUemFFls)bT)w0qOvCp49yHzDs94o03PEsLGT8IUN9dJH7Vj6hVCfTYHDLdkx3RfSuOY0Mn6tq49ADXo1FZOYpzBNzmm19kHLMib2OfiaJrdorjFHtNoEJM)bh(p7lyZUOOqlrQBMUDq4N)1r)HFqiZG9sOOtD0DjtemhV3lp)OF7NqBLnXy2(PKHLuSMbJsqCNjYdmcLpfa)XnJsD9XXZSKO2KoDUIqLLC6Ul8LlXg(mBlW5ZTGmB9Wx9710so94Zp(0MJF7n)7d

DEBUGGING

There is a DEBUG flag in loop.py that will enable additional logging to help troubleshoot issues with key presses.  
Additional, the util library includes a function to save an image of the screen or of a region into to __debug__ folder.
This will allow you to visualize what is being seen by the script.