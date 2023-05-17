import armstream
import numpy as np

# ---------------------------Builds Interception Context from CDSC_AL data ---------------------------#
def build_arm_interception_context(samples,
                                   std,
                                   predicted_category,
                                   local_subcluster_info,
                                   chunk_labels,
                                   labeled_indexes,
                                   samples_indexes,
                                   dim):

    labeled_mask = np.zeros(len(samples), dtype=bool)
    labeled_mask[labeled_indexes] = True
    samples_with_labels = list(zip(samples[samples_indexes], chunk_labels[samples_indexes], labeled_mask[samples_indexes]))

    samples_with_labels = list(filter(lambda x: x[0].max() <= 1, samples_with_labels))

    data_instances = list(map(
        lambda tuple_: armstream.DataInstance(tuple_[0].tolist(), int(tuple_[1]), bool(tuple_[2])),
        samples_with_labels))

    cluster_labels = list(local_subcluster_info.keys())

    data_classes_summary = []

    for l in cluster_labels:
        temp_clusterinfo = local_subcluster_info[str(l)]
        sublabels = list(temp_clusterinfo.keys())
        for lsub in sublabels:
            content = temp_clusterinfo[str(lsub)]
            attributes = content[0][:dim].tolist()
            label = content[0][dim]
            if np.array(attributes).max() <= 1:
                data_classes_summary.append(armstream.ClusterSummary(attributes, label, int(lsub)))
            else:
                print(attributes)



    context = armstream.InterceptionContext(
        cluster_summary=armstream.ClusterSummary(
            centroid_attributes=np.mean(samples[samples_indexes], axis=0).tolist(),
            standard_deviation=std,
            label=None
        ),
        cluster_data_instances=data_instances,
        predicted_category=predicted_category,
        data_classes_summary=data_classes_summary
    )

    return context