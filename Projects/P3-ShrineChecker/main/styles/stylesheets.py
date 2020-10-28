def convert_stylesheet(path):
    style = []
    with open(path, 'r', newline='\n') as f:
        for line in f:
            style.append(line)
        style = ''.join(style)
    return style

ui_stylesheet = convert_stylesheet('styles/ui_stylesheet.qss')
message_stylesheet = convert_stylesheet('styles/message_stylesheet.qss')
notification_stylesheet = convert_stylesheet('styles/notification_stylesheet.qss')
progress_stylesheet = convert_stylesheet('styles/progress_stylesheet.qss')
settings_stylesheet = convert_stylesheet('styles/settings_stylesheet.qss')
