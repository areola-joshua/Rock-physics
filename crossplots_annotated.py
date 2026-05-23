import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

df = pd.read_csv("well_log.csv")
df = df.dropna(subset=["GR", "AI", "VPVS", "LMR", "MUR", "PR", "NEI", "NPHI", "RHOB"])

bins_gr = [0, 50, 80, 110, 300]
labels_gr = ['Clean Sand', 'Sandy-Shale', 'Shaly-Sand', 'Shale']
df['FACIES_GR'] = pd.cut(df['GR'], bins=bins_gr, labels=labels_gr, include_lowest=True)

def annotate_box(ax, x, y, text, color='white', fontsize=10):
    ax.annotate(text, (x, y), textcoords="offset points", xytext=(8, 8),
                fontsize=fontsize, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=color, alpha=0.75, edgecolor='black'),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.2))

def trend_arrow(ax, start, end, text, color='darkred'):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=3, mutation_scale=22))
    mx, my = (start[0]+end[0])/2, (start[1]+end[1])/2
    ax.text(mx, my, text, fontsize=9, fontweight='bold', color=color,
            bbox=dict(boxstyle='round,pad=0.15', facecolor='white', alpha=0.8, edgecolor=color),
            ha='center', va='center')

def make_crossplot(df, x_col, y_col, x_label, y_label, title, filename,
                   annotations=None, show_lith=False):
    fig, ax = plt.subplots(figsize=(10, 8))

    norm = Normalize(vmin=df['GR'].min(), vmax=df['GR'].max())
    sc = ax.scatter(df[x_col], df[y_col], c=df['GR'], cmap='jet',
                    s=22, alpha=0.65, norm=norm, edgecolors='w', linewidth=0.15)
    cbar = fig.colorbar(sc, ax=ax, label='GR (API)', pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    if annotations:
        for a in annotations:
            if a['type'] == 'box':
                annotate_box(ax, a['x'], a['y'], a['text'], a.get('color', 'white'), a.get('fontsize', 10))
            elif a['type'] == 'arrow':
                trend_arrow(ax, a['start'], a['end'], a['text'], a.get('color', 'darkred'))

    if show_lith:
        rho_b = np.linspace(1.8, 3.0, 50)
        ax.plot(0.30 + (2.71 - rho_b)/4.0, rho_b, '--', color='blue', lw=1.5, alpha=0.6, label='Limestone')
        ax.plot(0.20 + (2.65 - rho_b)/2.5, rho_b, '--', color='red', lw=1.5, alpha=0.6, label='Sandstone')
        ax.plot(0.15 + (2.87 - rho_b)/3.0, rho_b, '--', color='green', lw=1.5, alpha=0.6, label='Dolomite')
        ax.legend(fontsize=8, loc='upper left', framealpha=0.8)
        ax.set_xlim(0.05, 0.65)
        ax.set_ylim(2.7, 1.8)

    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    ax.set_title(title, fontsize=13, fontweight='bold')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(filename, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"Saved: {filename}")

# ====== 1. AI vs Vp/Vs — fluid & lithology discrimination ======
make_crossplot(df, 'AI', 'VPVS', 'AI (Acoustic Impedance)', 'Vp/Vs',
               'AI vs Vp/Vs — GR Colored', 'ai_vs_vpvs.png',
               annotations=[
                   {'type': 'box', 'x': 5100, 'y': 2.62, 'text': 'Brine Sand', 'color': 'gold'},
                   {'type': 'box', 'x': 6200, 'y': 2.24, 'text': 'Silty / Transition', 'color': 'orange'},
                   {'type': 'box', 'x': 7000, 'y': 2.19, 'text': 'Shaly Reservoir', 'color': 'limegreen'},
                   {'type': 'box', 'x': 8100, 'y': 2.02, 'text': 'Dense Shale', 'color': 'brown'},
                   {'type': 'arrow', 'start': (9000, 2.45), 'end': (7500, 2.08), 'text': 'Compaction', 'color': 'darkred'},
               ])

# ====== 2. LMR vs MUR — lithology & fluid from elastic moduli ======
make_crossplot(df, 'MUR', 'LMR', r'$\mu\rho$ (Shear Modulus x Density)', r'$\lambda\rho$ (Incompressibility x Density)',
               'LMR vs MUR — GR Colored', 'lmr_vs_mur.png',
               annotations=[
                   {'type': 'box', 'x': 3.6, 'y': 18.2, 'text': 'Brine Sand', 'color': 'gold'},
                   {'type': 'box', 'x': 7.6, 'y': 22.6, 'text': 'Silty Sand', 'color': 'orange'},
                   {'type': 'box', 'x': 10.2, 'y': 27.8, 'text': 'Shaly Reservoir', 'color': 'limegreen'},
                   {'type': 'box', 'x': 15.8, 'y': 33.0, 'text': 'Dense Shale', 'color': 'brown'},
               ])

# ====== 3. Poisson Ratio vs AI — fluid sensitivity ======
make_crossplot(df, 'AI', 'PR', 'AI (Acoustic Impedance)', "Poisson's Ratio",
               "Poisson's Ratio vs AI — GR Colored", 'pr_vs_ai.png',
               annotations=[
                   {'type': 'box', 'x': 5100, 'y': 0.416, 'text': 'Brine Sand', 'color': 'gold'},
                   {'type': 'box', 'x': 6200, 'y': 0.375, 'text': 'Silty Interval', 'color': 'orange'},
                   {'type': 'box', 'x': 7000, 'y': 0.369, 'text': 'Shaly Sand', 'color': 'limegreen'},
                   {'type': 'box', 'x': 8100, 'y': 0.337, 'text': 'Shale', 'color': 'brown'},
                   {'type': 'arrow', 'start': (5400, 0.425), 'end': (4600, 0.395), 'text': 'Gas Effect', 'color': 'darkgreen'},
               ])

# ====== 4. Vp/Vs vs NEI — similar to AI-Vp/Vs ======
make_crossplot(df, 'NEI', 'VPVS', 'NEI (Near Elastic Impedance)', 'Vp/Vs',
               'Vp/Vs vs NEI — GR Colored', 'vpvs_vs_nei.png',
               annotations=[
                   {'type': 'box', 'x': 5950, 'y': 2.62, 'text': 'Brine Sand', 'color': 'gold'},
                   {'type': 'box', 'x': 6450, 'y': 2.24, 'text': 'Silty Interval', 'color': 'orange'},
                   {'type': 'box', 'x': 6950, 'y': 2.19, 'text': 'Shaly Reservoir', 'color': 'limegreen'},
                   {'type': 'box', 'x': 7550, 'y': 2.02, 'text': 'Shale', 'color': 'brown'},
               ])

# ====== 5. RHOB vs NPHI — neutron-density lithology ======
make_crossplot(df, 'NPHI', 'RHOB', 'NPHI (Neutron Porosity)', 'RHOB (Bulk Density)',
               'RHOB vs NPHI — GR Colored', 'rhob_vs_nphi.png',
               show_lith=True,
               annotations=[
                   {'type': 'box', 'x': 0.38, 'y': 2.07, 'text': 'Brine Sand', 'color': 'gold'},
                   {'type': 'box', 'x': 0.37, 'y': 2.16, 'text': 'Silty Sand', 'color': 'orange'},
                   {'type': 'box', 'x': 0.46, 'y': 2.38, 'text': 'Shaly Sand', 'color': 'limegreen'},
                   {'type': 'box', 'x': 0.40, 'y': 2.52, 'text': 'Shale', 'color': 'brown'},
                   {'type': 'arrow', 'start': (0.50, 2.00), 'end': (0.35, 2.55), 'text': 'Compaction', 'color': 'darkred'},
               ])

print("\nAll crossplots done!")
