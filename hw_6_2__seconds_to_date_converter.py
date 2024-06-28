def convert_seconds_to_dd_hh_mm_ss_format(orig_value):
    result = "Invalid value: should be non-negative integer less than 8640000"
    if orig_value.isdigit():
        minute_val = 60
        hour_val = minute_val * 60
        day_val = hour_val * 24

        input_int = int(orig_value)
        days, hh_mm_ss = divmod(input_int, day_val)
        hours, mm_ss = divmod(input_int - days * day_val, hour_val)
        minutes, seconds = divmod(input_int - days * day_val - hours * hour_val, minute_val)

        days_declension = 'днів'
        days_digits = divmod(days, 10)

        if days_digits[0] != 1:
            match days_digits[1]:
                case 2 | 3 | 4:
                    days_declension = 'дні'

                case 1:
                    days_declension = 'день'

        result = str(days) + " " \
                 + days_declension + " " \
                 + str(hours).zfill(2) + ":" \
                 + str(minutes).zfill(2) + ":" \
                 + str(seconds).zfill(2)

    return result


user_input = input('Enter amount of seconds to transform to DD HH:MM:SS format:\n')

print(convert_seconds_to_dd_hh_mm_ss_format(user_input))
