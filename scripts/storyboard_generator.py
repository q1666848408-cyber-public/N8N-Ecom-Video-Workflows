"""
6-grid storyboard generator — called from n8n Code nodes.
Showcase version: skeleton only.
"""

from typing import List, Dict


class StoryboardGenerator:
    GRID_SIZE = 6  # 2x3 cells

    def generate(self, product_info: dict, reference_video_url: str = None) -> List[Dict]:
        """Produce 6 cells with prompts + composition notes. [Not shown]"""
        pass

    def _watermark_strip(self, frame_bytes: bytes) -> bytes:
        """Remove watermark from reference video frames. [Not shown]"""
        pass

    def _compose_grid(self, cells: List[Dict]) -> bytes:
        """Composite 6 cells into single image for Gemini. [Not shown]"""
        pass
