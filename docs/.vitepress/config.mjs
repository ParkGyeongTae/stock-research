import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const docsDir = path.dirname(path.dirname(fileURLToPath(import.meta.url)))

function parsePages(directory) {
  const pagesFile = path.join(directory, '.pages')
  if (!fs.existsSync(pagesFile)) return null

  return fs.readFileSync(pagesFile, 'utf8')
    .split('\n')
    .map((line) => line.match(/^\s+-\s+(?:(.+?):\s+)?([^\s]+)\s*$/))
    .filter(Boolean)
    .map(([, label, target]) => ({ label: label?.trim(), target }))
}

function pageTitle(file) {
  const match = fs.readFileSync(file, 'utf8').match(/^#\s+(.+)$/m)
  return match?.[1]?.replace(/[`*_]/g, '') || path.basename(file, '.md')
}

function autoNavFor(directory, excludedTargets = new Set()) {
  return fs.readdirSync(directory, { withFileTypes: true })
    .filter((entry) => !entry.name.startsWith('.') && !excludedTargets.has(entry.name) && (entry.isDirectory() || entry.name.endsWith('.md')))
    .sort((a, b) => a.name.localeCompare(b.name, 'en'))
    .map((entry) => {
      const absolute = path.join(directory, entry.name)
      if (entry.isDirectory()) {
        const report = path.join(absolute, '00_final_report.md')
        const overview = path.join(absolute, '01_overview.md')
        const children = autoNavFor(absolute)
        return {
          text: fs.existsSync(overview) ? pageTitle(overview) : (fs.existsSync(report) ? pageTitle(report) : entry.name),
          ...(children.length ? { items: children } : {}),
        }
      }
      return {
        text: pageTitle(absolute),
        link: `/${path.relative(docsDir, absolute).replaceAll(path.sep, '/').replace(/\.md$/, '')}`,
      }
    })
}

function navFor(directory) {
  const entries = parsePages(directory)
  if (!entries) return autoNavFor(directory)

  return entries.map(({ label, target }) => {
    if (target === '...') {
      const explicitTargets = new Set(entries.filter((entry) => entry.target !== '...').map((entry) => entry.target))
      return { items: autoNavFor(directory, explicitTargets) }
    }
    const absolute = path.join(directory, target)
    if (target.endsWith('.md')) {
      return {
        text: label || pageTitle(absolute),
        link: `/${path.relative(docsDir, absolute).replaceAll(path.sep, '/').replace(/\.md$/, '')}`,
      }
    }

    const children = navFor(absolute)
    return {
      text: label || path.basename(target),
      ...(children.length ? { items: children } : { link: `/${path.relative(docsDir, absolute).replaceAll(path.sep, '/')}/` }),
    }
  })
}

const navigation = navFor(docsDir)

function collapseSidebarGroups(items) {
  return items.map((item) => item.items
    ? { ...item, collapsed: true, items: collapseSidebarGroups(item.items) }
    : item)
}

const sidebar = collapseSidebarGroups(navigation)

const siteUrl = 'https://parkgyeongtae.github.io'
const siteBase = '/stock-research/'

export default {
  lang: 'ko-KR',
  title: '주식 리서치 노트',
  description: '미국 상장 기업/섹터 투자 리서치 정리',
  base: siteBase,
  cleanUrls: true,
  lastUpdated: true,
  sitemap: {
    hostname: `${siteUrl}${siteBase}`,
  },
  transformHead({ pageData }) {
    const pagePath = pageData.relativePath
      .replace(/(^|\/)index\.md$/, '$1')
      .replace(/\.md$/, '')
    const canonicalPath = pagePath ? `${siteBase}${pagePath}` : siteBase

    return [
      ['link', { rel: 'canonical', href: `${siteUrl}${canonicalPath}` }],
    ]
  },
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: `${siteBase}stock-research-icon.png` }],
  ],
  themeConfig: {
    logo: {
      src: '/stock-research-icon.png',
      alt: '주식 리서치 노트 로고',
    },
    nav: navigation,
    sidebar,
    search: { provider: 'local' },
    socialLinks: [{ icon: 'github', link: 'https://github.com/ParkGyeongTae/stock-research' }],
    footer: {
      message: '개인 투자 리서치 아카이브 — 투자 권유가 아닙니다.',
    },
  },
}
