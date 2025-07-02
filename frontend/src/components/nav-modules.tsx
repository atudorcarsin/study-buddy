import { ChevronRight, MoreHorizontal, Plus } from "lucide-react"

import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible"
import {
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuAction,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
} from "@/components/ui/sidebar"

export function NavModules({
  modules,
}: {
  modules: {
    name: string
    emoji: React.ReactNode
    pages: {
      name: string
      emoji: React.ReactNode
    }[]
  }[]
}) {
  return (
    <SidebarGroup>
      <SidebarGroupLabel>Modules</SidebarGroupLabel>
      <SidebarGroupContent>
        <SidebarMenu>
          {modules.map((module) => (
            <Collapsible key={module.name}>
              <SidebarMenuItem>
                <SidebarMenuButton asChild>
                  <a href="#">
                    <span>{module.emoji}</span>
                    <span>{module.name}</span>
                  </a>
                </SidebarMenuButton>
                <CollapsibleTrigger asChild>
                  <SidebarMenuAction
                    className="bg-sidebar-accent text-sidebar-accent-foreground left-2 data-[state=open]:rotate-90"
                    showOnHover
                  >
                    <ChevronRight />
                  </SidebarMenuAction>
                </CollapsibleTrigger>
                <SidebarMenuAction showOnHover>
                  <Plus />
                </SidebarMenuAction>
                <CollapsibleContent>
                  <SidebarMenuSub>
                    {module.pages.map((page) => (
                      <SidebarMenuSubItem key={page.name}>
                        <SidebarMenuSubButton asChild>
                          <a href="#">
                            <span>{page.emoji}</span>
                            <span>{page.name}</span>
                          </a>
                        </SidebarMenuSubButton>
                      </SidebarMenuSubItem>
                    ))}
                  </SidebarMenuSub>
                </CollapsibleContent>
              </SidebarMenuItem>
            </Collapsible>
          ))}

          <SidebarMenuItem>
            <SidebarMenuButton className="text-sidebar-foreground/70">
              <MoreHorizontal />
              <span>More</span>
            </SidebarMenuButton>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarGroupContent>
    </SidebarGroup>
  )
}
