# -*- coding: utf-8 -*-

# Copyright 2016 Google, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import snippets


def test_sentiment_text(cloud_config, capsys):
    snippets.sentiment_text('Hello, world!')
    out, _ = capsys.readouterr()
    assert 'Polarity: 1' in out


def test_sentiment_file(cloud_config, capsys):
    snippets.sentiment_file('gs://bucket/file.txt')
    out, _ = capsys.readouterr()
    assert 'Polarity: 1' in out


def test_entities_text(cloud_config, capsys):
    snippets.entities_text('President Obama is speaking at the White House.')
    out, _ = capsys.readouterr()
    assert 'name: Obama' in out


def test_entities_file(cloud_config, capsys):
    snippets.entities_file('gs://bucket/file.txt')
    out, _ = capsys.readouterr()
    assert 'Polarity: 1' in out


def test_syntax_text(cloud_config, capsys):
    snippets.syntax_text('Hello, world!')
    out, _ = capsys.readouterr()
    assert 'Polarity: 1' in out


def test_syntax_file(cloud_config, capsys):
    snippets.syntax_file('gs://bucket/file.txt')
    out, _ = capsys.readouterr()
    assert 'Polarity: 1' in out
