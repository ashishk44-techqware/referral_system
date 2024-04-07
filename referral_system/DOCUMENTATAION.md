# REFERRAL SYSTEM API DOCUMENTATION

# User Registration API

- **Method**: POST
- **URL**: `/api/v1/register`
- **Description**: User will register in referral system database.
- **Request Body**:
  - Required fields:
    - `name`: Name of the user.
    - `email`: Email address of the user.
    - `password`: Password for the user account.
  - Optional fields:
    - `referral_code`: Referral code, if provided by an existing user for referral benefits.
- **Response**:
  - Success (Status Code: 201 Created):
    - Body: `{ "user_id": <user_id>, "message": "User registered successfully" }`
  - Failure (Status Code: 400 Bad Request or 404 Not Found):
    - Body: `{ "message": <error_message> }`

# User Login Endpoint

- **Method**: POST
- **URL**: `/api/v1/login`
- **Description**: User will login via this url and `access` and `referesh` token get generated      which is used for authintication purpose in other api's.

- **Request Body**:
  - Required fields:
    - `email`: Email address of the user.
    - `password`: Password for the user account.
- **Response**:
  - Success (Status Code: 200 OK):
    - Body: `{ "refresh": <refresh_token>, "access": <access_token>, "user_id": <user_id>, "message": "Login successful." }`
  - Failure (Status Code: 401 Unauthorized):
    - Body: `{ "message": "Invalid credentials." }`

# User Profile Endpoint

- **Method**: GET
- **URL**: `/api/v1/user-profile`
- **Description**: Retrieves the profile details of the authenticated user.
- **Authorization**: 
    - Requires a valid JWT access token in the Authorization header  Or Bearer token.
    - While using postman select the Bearer token in autorization section
- **Response**:
  - Success (Status Code: 200 OK):
    - Body: `{ "message": "user profile", "data": { "user_id": <user_id>, "email": <email>, "referral_code": <referral_code>, "created_at": <timestamp> } }`
  - Failure (Status Code: 401 Unauthorized):
    - Body: `{ "message": "Invalid credentials." }`

# Referrals Endpoint

- **Method**: GET
- **URL**: `/api/v1/referred-users`
- **Description**: Retrieves a paginated list of users referred by the authenticated user.
- **Authorization**: 
    - Requires a valid JWT access token in the Authorization header  Or Bearer token.
    - While using postman select the Bearer token in autorization section

- **Query Parameters**:
  - `page`: (Optional) Page number for pagination (default: 1).
  - `Example url for page`: `/api/v1/referred-users?page=1`

- **Response**:
  - Success (Status Code: 200 OK):
    - Body: `{ "message": "referral user list", "data": [{ "referred_user_id": <user_id>, "referred_user_email": <email>, "timestamp": <timestamp> }, ...] }`
    
    - Note:- `refeerred_user_id`  is user profile id of the user who used the referal token of logind user 
  
  - Failure (Status Code: 401 Unauthorized):
    - Body: `{ "message": "Invalid credentials." }`
