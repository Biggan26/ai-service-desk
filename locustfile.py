from locust import HttpUser, between, task


class TicketApiUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def check_health(self) -> None:
        self.client.get("/health", name="GET /health")

    @task(2)
    def check_ready(self) -> None:
        self.client.get("/ready", name="GET /ready")

    @task(4)
    def list_tickets(self) -> None:
        self.client.get("/tickets", name="GET /tickets")

    @task(2)
    def create_ticket(self) -> None:
        self.client.post(
            "/tickets",
            name="POST /tickets",
            json={
                "title": "Load Test Ticket",
                "description": "This ticket was created during Locust load testing.",
                "priority": "High",
                "assigned_to": "Load Tester",
                "assigned_to_email": "loadtester@example.com",
            },
        )

    @task(1)
    def home(self) -> None:
        self.client.get("/", name="GET /")
