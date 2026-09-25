def get_delivery_status(distance):
    if distance <= 3:
        return "Fast delivery"
    elif  distance <= 10:
        return "Standard delivery"
    else:
        return "Slow delivery"