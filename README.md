## Inspiration
Let's face it, this pandemic has been a real struggle for everyone, especially those who miss interacting with others on a daily basis. In fact, the CDC asserts that because of social distancing, people are more likely to feel isolated, and in turn, cause stress and anxiety. We needed to find a solution that allows people to manage these symptoms and keep people happy during this lonesome time.
## What it does
**Charlie AI** is a program that emulates a friend that you can talk to! Charlie is capable of listening and responding based on context cues, carrying a conversation, and mimic human behavioral patterns based off of trained models. **Charlie AI** is similar to a psychiatrist AI that is designed to help cope through the pressures of lockdown in a pandemic.
## How I built it
We used Python for this project. Using python's native text-to-speech (TTS) package, we converted the client's audio into text that was usable in the logic of our program. Our logic incorporates contextual cues and keywords to determine an appropriate response. Then, with the help of a utility called CrazyTalk, we animated Charlie AI's 3D avatar to respond to the client. The avatar itself is programmed to have idle movement patterns in order to better emulate humans themselves. 
## Challenges I ran into
We had to make a compromise between accuracy and compatibility for the speech-recognition aspect of our program. We initially went with Google's 'gTTS' API but we ran into constant issues with how our asynchronous function was interacting with the rest of the program during runtime. So, we decided to use Python's own text-to-speech package at the cost of marginal speech-recognition accuracy.

We also had problems finding and using adequate 3D animation software that could supply the tools we needed, namely a way to input our audio generated from our Python script. The program we eventually decided to use had the right balance of convenience and functionality. 

## Accomplishments that I'm proud of
This was our first collective experience with 3D animation software and interfacing it with python scripts. We had a great time learning and using these new tools.
## What I learned
Compromising between functionality and convenience. Learning basic 3D animation software.
## What's next for Charlie
Refine animations, expand the number of responses, and publish to the Apple App / Google Play Store.