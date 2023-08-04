from grafana_api.grafana_face import GrafanaFace
import json

grafana_api = GrafanaFace(auth=("admin", "Grafana1717!"), host='34.140.233.235:30008')

with open('dashboards/kube-dashboard.json') as file:
    json_dashboard = json.load(file)
try:
    grafana_api.dashboard.update_dashboard(dashboard=json_dashboard)
    print("The dashboard creation succeeded")
except Exception as e:
    print(f"The dashboard creation failed with error: {str(e)}")

