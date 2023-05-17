from enum import Enum
from typing import Optional
import requests
import json


class ClusterSummary(dict):
    def __init__(self, centroid_attributes: [float], standard_deviation: float, label: Optional[int]):
        dict.__init__(self, centroid_attributes=centroid_attributes, standard_deviation=standard_deviation, label=label)
        self.centroid_attributes = centroid_attributes
        self.standard_deviation = standard_deviation
        self.label = label


class DataInstance(dict):
    def __init__(self, attributes: [float], true_label: int, true_label_available: bool):
        dict.__init__(self, attributes=attributes, true_label=true_label, true_label_available=true_label_available)
        self.attributes = attributes
        self.true_label = true_label
        self.true_label_available = true_label_available


class Category(str, Enum):
    KNOWN = 'KNOWN'
    NOVELTY = 'NOVELTY'


class InterceptionContext(dict):
    def __init__(self,
                 cluster_summary: ClusterSummary,
                 cluster_data_instances: [DataInstance],
                 predicted_category: Category,
                 data_classes_summary: [ClusterSummary]) -> None:
        dict.__init__(self, cluster_summary=cluster_summary,
                      cluster_data_instances=cluster_data_instances,
                      predicted_category=predicted_category,
                      data_classes_summary=data_classes_summary)
        self.cluster_summary = cluster_summary
        self.cluster_data_instances = cluster_data_instances
        self.predicted_category = predicted_category
        self.data_classes_summary = data_classes_summary


class RemoteInterceptor:
    def __init__(self):
        self.base_url = ''

    def set_base_url(self, base_url):
        self.base_url = base_url.rstrip('/')

    def intercept(self, context: InterceptionContext):
        if not self.base_url:
            return None
        url = f'{self.base_url}/intercept'
        response = requests.post(url, json=context)
        response.raise_for_status()
        return {}

    def peek(self, properties: dict):
        if not self.base_url:
            return None
        url = f'{self.base_url}/peek'
        response = requests.post(url, json=properties)
        response.raise_for_status()
        return {}

    def finish(self):
        if not self.base_url:
            return None
        url = f'{self.base_url}/finish'
        response = requests.post(url)
        response.raise_for_status()
        return {}