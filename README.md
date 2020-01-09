# Pizza Party 
## CS Build Week 1

Backend for Pizza Party, an interactive ***Multi-User Dungeon (MUD)*** client produced for CS24 Build Week 1 at Lambda School

## API Reference

### Auth Endpoints
| Method | URL | Description |
| ----- | ----- | ----- |
| POST | api/registration/ | Creates user with the `username`, `email` (optional), and matching `password1` and `password2` sent in the request body. Returns a `key`. |
| POST | api/login/ | Logs in user with the credential sent inside the request body. Returns a `key`. |
| POST | api/logout/ | Calls Django logout method and delete the Token object assigned to the current User object. Accepts/Returns nothing. |
| GET | api/user/ | Returns the current user's information |

### Game Endpoints
| Method | URL | Description |
| ----- | ----- | ----- |
| GET | api/adv/init | Initializes a player in the first room |
| POST | api/adv/move | Moves the player in the specified `direction` (`n`/`e`/`s`/`w`) if the move is allowed. |
| GET | api/rooms/ | For logged in users, returns object containing all the rooms in the game |

### Example Requests

* Register
    curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password1":"testpassword", "password2":"testpassword"}' http://pizza-party-bw.herokuapp.com/api/registration/

* Login
    curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password":"testpassword"}' http://pizza-party-bw.herokuapp.com/api/login/

* Initialize (Replace token string with logged in user's auth token)
    curl -X GET -H 'Authorization: Token 6b7b9d0f33bd76e75b0a52433f268d3037e42e66' http://pizza-party-bw.herokuapp.com/api/adv/init/

* Move (Replace token string with logged in user's auth token)
    curl -X POST -H 'Authorization: Token 6b7b9d0f33bd76e75b0a52433f268d3037e42e66' -H "Content-Type: application/json" -d '{"direction":"n"} http://pizza-party-bw.herokuapp.com/api/adv/move/

* Get Rooms (Replace token string with logged in user's auth token)
    curl -X GET -H 'Authorization: Token cc504e88ef659843b858d61c101ca9d4f0edf979' http://pizza-party-bw.herokuapp.com/api/adv/move/


## Room Model
| Field | Type | Description |
| ----- | ----- | ----- |
| id | primary key | auto-incrementing room ID |
| title | string | Title of the room |
| description | string | Description of the room |
| x | integer | x coordinate of room, with map starting at (0,0) in top left  |
| y | integer | y coordinate of room |
| n_to | integer | ID of room to the north. Defaults to 0 (no connection) |
| s_to | integer | ID of room to the south. Defaults to 0 (no connection) |
| e_to | integer | ID of room to the east. Defaults to 0 (no connection) |
| w_to | integer | ID of room to the west. Defaults to 0 (no connection) |


## Player Model
| Field | Type | Description |
| ----- | ----- | ----- |
| user | integer | User model ID - OneToOneField |
| current_room | integer | ID of the player's room |
| uuid | UUIDField | universally unique identifier |