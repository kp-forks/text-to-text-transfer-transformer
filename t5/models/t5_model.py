# Copyright 2024 The T5 Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""T5 Model Abstract Base class."""

import abc


class T5Model(metaclass=abc.ABCMeta):
  """Abstract Base class for T5 Model API."""

  @abc.abstractmethod
  def train(self, mixture_or_task_name, steps):
    raise NotImplementedError()

  @abc.abstractmethod
  def eval(self, mixture_or_task_name):
    raise NotImplementedError()

  @abc.abstractmethod
  def predict(self):
    raise NotImplementedError()

  @abc.abstractmethod
  def finetune(self, mixture_or_task_name, finetune_steps):
    raise NotImplementedError()
