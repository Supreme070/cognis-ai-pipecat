#
# Copyright (c) 2024–2025, Daily
#
# SPDX-License-Identifier: BSD 2-Clause License
#

"""Model-proxy unified AI services for Pipecat.

This module provides unified access to various AI services through a single
the model proxy API endpoint, abstracting away provider-specific implementations.
"""

from pipecat.services.model_proxy.llm import ModelProxyLLMService
from pipecat.services.model_proxy.stt import ModelProxySTTService, ModelProxySTTSettings
from pipecat.services.model_proxy.tts import ModelProxyTTSService, ModelProxyTTSSettings

__all__ = [
    "ModelProxyLLMService",
    "ModelProxySTTService",
    "ModelProxySTTSettings",
    "ModelProxyTTSService",
    "ModelProxyTTSSettings",
]
