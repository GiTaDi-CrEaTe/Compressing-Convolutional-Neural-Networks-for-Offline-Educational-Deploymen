import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# The Final Verified 10,000-Image Data
labels = ['Baseline\n(FP32)', 'Quantized\n(INT8)', 'Pruned 70%\n(FP32)', 'Pruned 70%\n+ INT8']
accuracies = [98.78, 98.69, 98.77, 98.78]
sizes_bytes = [224892, 61800, 224892, 61800]
sizes_kb = [size / 1024 for size in sizes_bytes] # Convert to KB for cleaner charts

colors = ['#4A90E2', '#50E3C2', '#F5A623', '#D0021B']

# ---------------------------------------------------------
# Figure 1: CNN Architecture Block Diagram
# ---------------------------------------------------------
print("Generating Figure 1: Architecture Diagram...")
fig1, ax1 = plt.subplots(figsize=(12, 3))
ax1.axis('off')

blocks = [
    ("Input\n28x28x1", 0),
    ("Conv2D\n16 Filters", 2.5),
    ("MaxPool\n2x2", 5),
    ("Conv2D\n32 Filters", 7.5),
    ("MaxPool\n2x2", 10),
    ("Flatten", 12.5),
    ("Dense\n32 Units", 15),
    ("Dense\n10 Units", 17.5)
]

for i, (text, x) in enumerate(blocks):
    rect = patches.Rectangle((x, 0.2), 2, 0.6, linewidth=1.5, edgecolor='black', facecolor='#f0f4f8')
    ax1.add_patch(rect)
    ax1.text(x + 1, 0.5, text, ha='center', va='center', fontsize=10, weight='bold')
    if i < len(blocks) - 1:
        ax1.annotate('', xy=(x + 2.5, 0.5), xytext=(x + 2, 0.5),
                     arrowprops=dict(arrowstyle="->", lw=2))

ax1.set_xlim(0, 20)
ax1.set_ylim(0, 1)
plt.title("Figure 1: Edge CNN Architecture", weight='bold', pad=20)
plt.savefig('figure1.png', dpi=300, bbox_inches='tight')
plt.close()

# ---------------------------------------------------------
# Figure 2: Model Size Comparison (Bar Chart)
# ---------------------------------------------------------
print("Generating Figure 2: Size Comparison...")
fig2, ax2 = plt.subplots(figsize=(8, 5))
bars = ax2.bar(labels, sizes_kb, color=colors, edgecolor='black')

ax2.set_ylabel('Model Size (Kilobytes)', weight='bold')
ax2.set_title('Figure 2: Model Size Across Compression Strategies', weight='bold')
ax2.set_ylim(0, 260)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

for bar, size_bytes in zip(bars, sizes_bytes):
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 3, f"{size_bytes:,} B", ha='center', va='bottom', weight='bold')

plt.savefig('figure2.png', dpi=300, bbox_inches='tight')
plt.close()

# ---------------------------------------------------------
# Figure 3: Test Accuracy (Zoomed Bar Chart)
# ---------------------------------------------------------
print("Generating Figure 3: Accuracy Comparison...")
fig3, ax3 = plt.subplots(figsize=(8, 5))
bars_acc = ax3.bar(labels, accuracies, color=colors, edgecolor='black')

ax3.set_ylabel('Test Accuracy (%)', weight='bold')
ax3.set_title('Figure 3: Test Accuracy Retention', weight='bold')
# Zoom in tightly to show the tiny 0.09% differences
ax3.set_ylim(98.5, 99.0)
ax3.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars_acc:
    yval = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2, yval + 0.01, f"{yval:.2f}%", ha='center', va='bottom', weight='bold')

plt.savefig('figure3.png', dpi=300, bbox_inches='tight')
plt.close()

# ---------------------------------------------------------
# Figure 4: Trade-off Matrix (Pareto Style)
# ---------------------------------------------------------
print("Generating Figure 4: Compression vs. Accuracy Trade-off...")
fig4, ax4_size = plt.subplots(figsize=(9, 6))

ax4_acc = ax4_size.twinx()

# Plot Size as bars
ax4_size.bar(labels, sizes_kb, color='#B0C4DE', edgecolor='black', alpha=0.7, label='Size (KB)')
ax4_size.set_ylabel('Model Size (KB)', weight='bold')
ax4_size.set_ylim(0, 260)

# Plot Accuracy as a red line over the bars
ax4_acc.plot(labels, accuracies, color='#D0021B', marker='o', linewidth=3, markersize=8, label='Accuracy (%)')
ax4_acc.set_ylabel('Test Accuracy (%)', weight='bold', color='#D0021B')
ax4_acc.set_ylim(98.5, 99.0)
ax4_acc.tick_params(axis='y', labelcolor='#D0021B')

for i, txt in enumerate(accuracies):
    ax4_acc.annotate(f"{txt:.2f}%", (i, accuracies[i]), textcoords="offset points", xytext=(0,10), ha='center', weight='bold', color='#D0021B')

plt.title('Figure 4: Edge AI Compression Trade-off', weight='bold')
plt.savefig('figure4.png', dpi=300, bbox_inches='tight')
plt.close()

print("\nSuccess! figure1.png, figure2.png, figure3.png, and figure4.png are ready on your Desktop.")