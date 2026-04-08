class Event:
    def __init__(self, event_id, timestamp, zone_id, event_type, duration, gender, age):
        # Identificador único do evento
        self.event_id = event_id

        # Data e hora no formato string "YYYY-MM-DD HH:MM:SS"
        self.timestamp = timestamp

        # Zona onde ocorreu o evento
        self.zone_id = zone_id

        # Tipo de evento: entrada, saída ou permanência
        self.event_type = event_type  # "entry" | "exit" | "linger"

        # Tempo de permanência (em segundos)
        # Só faz sentido para eventos "linger"
        self.duration = int(duration)

        # Dados demográficos
        self.gender = gender  # "M" | "F"
        self.age = age        # "child", "adult", etc.

        # ── CAMPOS DERIVADOS (otimização) ─────────────────────

        # Data separada (mais fácil para indexação)
        self.date = timestamp[:10]

        # Hora extraída (int)
        self.hour = int(timestamp[11:13])

        # Minuto extraído
        self.minute = int(timestamp[14:16])

        # Dia da semana (preenchido depois no data_loader)
        self.weekday = None

    def __repr__(self):
        # Representação para debug
        return f"<Event {self.event_id} {self.event_type} {self.zone_id} {self.timestamp}>"