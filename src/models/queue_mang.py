class QueueManager:
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.queue = []  # Lista para la cola de usuarios activos
        self.waitlist = []  # Lista de espera

    def add_user(self, user):
        """Añade un usuario a la cola o a la lista de espera."""
        if len(self.queue) < self.max_size:
            self.queue.append(user)
            return f"{user} agregado a la cola."
        else:
            self.waitlist.append(user)
            return f"{user} agregado a la lista de espera."

    def remove_user(self):
        """Elimina el primer usuario de la cola y mueve uno de la lista de espera."""
        if self.queue:
            removed_user = self.queue.pop(0)  # Sacar el primer usuario de la cola
            if self.waitlist:
                self.queue.append(self.waitlist.pop(0))  # Mover el primero de la lista de espera
            return f"{removed_user} eliminado de la cola."
        return "La cola está vacía."

    def get_queue(self):
        """Devuelve la lista de usuarios en la cola."""
        return self.queue

    def get_waitlist(self):
        """Devuelve la lista de espera."""
        return self.waitlist
