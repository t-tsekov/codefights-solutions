if upSpeed > desiredHeight:
        return 1
    return desiredHeight // (upSpeed - downSpeed)