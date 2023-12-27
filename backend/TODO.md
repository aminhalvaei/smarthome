# TODO List

- Specify Email verification flow
- Complete home app and add its views and urls
- Make and Document a clear permissions policy
- Make seperate endpoints for controllers and devices that are registered and not registered or maybe i can change the serializer so that is_active and is_registered are included.
- Complete the weather app views urls and serializers for its new models(pref,prefval,weatherCondition,configs)
- Define default parameters and parameter categories in database initialization phase
- Make seperate files for client and controller services in project directory
- Make a more consice and better system for units of measurement
- handle the is_active and is_registered flags of controller so that if those flags are false for a controller it cant access the server and get weather_condition