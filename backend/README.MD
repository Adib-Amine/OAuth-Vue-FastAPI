
### Installation
The easiest way to start working with this exemple:<br>
`pip install - r requirements.txt`


### About JWT
**JWT**  means **"JSON Web Tokens"**.
It's a standard to codify a JSON object in a long dense string without spaces. It looks like this:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```
It is not encrypted, so, anyone could recover the information from the contents.<br>
But it's signed. So, when you receive a token that you emitted, you can verify that you actually emitted it.<br>
That way, you can create a token with an expiration of, let's say, 1 week. And then when the user comes back the next day with the token, you know that user is still logged in to your system.<br>
After a week, the token will be expired and the user will not be authorized and will have to sign in again to get a new token. And if the user (or a third party) tried to modify the token to change the expiration, you would be able to discover it, because the signatures would not match.<br>
If you want to play with JWT tokens and see how they work, check [https://jwt.io](https://jwt.io).<br>
